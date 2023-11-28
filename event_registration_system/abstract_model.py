from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class AbstractTimeMixin(models.Model):
    is_active = models.BooleanField(
        _('Is Active'), 
        default=True
    )
    created_at = models.DateTimeField(
        _('Created At'), 
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated At'), 
        auto_now=True
    )

    class Meta:
        abstract = True
