from datetimepicker.widgets import DateTimePicker
from django.forms import Form, ChoiceField
from django import forms

from .models import Order
from authentication.models import CustomUser
from book.models import Book



class FilterForm(Form):
    OPTIONS = (
        ('3', '3 days'),
        ('5', '5 days'),
        ('7', '1 week'),
        ('30', '1 month'),
    )
    select = ChoiceField(choices=OPTIONS)


class CustomUserSelectForm(forms.ModelChoiceField):

    def label_from_instance(self, user):
        return f'{user.first_name} {user.middle_name} {user.last_name}'


class CustomBookSelectForm(forms.ModelChoiceField):

    def label_from_instance(self, book):
        book_authors = [' '.join((author.name, author.surname)) for author in book.authors.all()]
        return f"\"{book.name}\" - {', '.join(book_authors)}"


class OrderCreationForm(forms.ModelForm):

    user = CustomUserSelectForm(
        queryset=CustomUser.get_all(),
        widget=forms.Select()
    )

    book = CustomBookSelectForm(
        queryset=Book.get_all(),
        widget=forms.Select()
    )

    class Meta:
        model = Order
        exclude = ['uuid', 'created_at']

        widgets = {
            'nd_at': forms.DateTimeInput(),
            'plated_end_at': forms.DateTimeInput()
        }
