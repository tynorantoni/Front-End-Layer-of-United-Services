from django import forms

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class TicketForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'What is wrong with bicycle?'}))
    desc = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Describe your problem'}))
    bike_name = forms.ChoiceField(choices=[(1,"CX"),(2,"SingleSpeed")])
    priority = forms.ChoiceField(choices=[(1,"You can ride with this"),(2,"Normal"),(3,"AS ASAP AS POSSIBLE")])

    class Meta:
        model = Ticket
        fields = 'title','desc','bike_name','priority'