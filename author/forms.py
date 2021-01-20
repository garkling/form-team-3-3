from django import forms

from .models import Author


class AuthorCreationForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = ['uuid']
        widgets = {
            'name': forms.TextInput(),
            'surname': forms.TextInput(),
            'patronymic': forms.TextInput()
        }
