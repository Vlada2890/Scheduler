from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
