from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'dose', 'dose_units', 'prescriber', 'pharmacy', 'price', 'expiration_date']
        labels = {'name': 'Medication', 'dose_units': 'Dose Units', 'expiration_date': 'Expiration Date'}

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)