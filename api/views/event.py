from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from event_manager.models import Event, EventRegistration
from api.serializers import (
    EventSerializer, EventRegistrationSerializer
)


# All Event List
class EventListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all().order_by('pk')
    serializer_class = EventSerializer


# Event Details View
class EventDetailsView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all().order_by('pk')
    serializer_class = EventSerializer
    lookup_field = 'pk'


# Event Registration View
class UserEventRegistrationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, event_id):
        event = generics.get_object_or_404(
            Event, pk=event_id
        )
        registration_data = {'event': event.id, 'user': request.user.id}
        serializer = EventRegistrationSerializer(
            data=registration_data
        )

        if serializer.is_valid():
            serializer.save()
            event.available_slots -= 1
            event.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Users Event
class UserRegisteredEventsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(
            eventregistration__user=user
        )
