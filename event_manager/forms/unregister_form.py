from django import forms

class UnregistrationForm(forms.Form):
    event = forms.CharField(
        widget=forms.HiddenInput(), required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('event')

        return cleaned_data
