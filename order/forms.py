from datetimepicker.widgets import DateTimePicker
from django.forms import Form, ChoiceField
from django import forms
from .models import Order



class FilterForm(Form):
    OPTIONS = (
        ('3', '3 days'),
        ('5', '5 days'),
        ('7', '1 week'),
        ('30', '1 month'),
    )
    select = ChoiceField(choices=OPTIONS)


class OrderCreationForm(forms.ModelForm):
    user = forms.ChoiceField(widget=forms.Select()),
    book = forms.ChoiceField(widget=forms.Select()),

    class Meta:
        model = Order
        exclude = ['uuid']

        widgets = {
            'nd_at': forms.DateTimeInput(),
            'plated_end_at': forms.DateTimeInput()
        }
