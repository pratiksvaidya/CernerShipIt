from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'dose', 'dose_units', 'prescriber', 'pharmacy', 'price', 'expiration_date']
        labels = {'name': 'Medication', 'dose_units': 'Dose Units', 'expiration_date': 'Expiration Date'}
