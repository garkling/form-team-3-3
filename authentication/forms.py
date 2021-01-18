from django.forms import ModelForm, TextInput

from .models import CustomUser


class UserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'password'
        ]
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'validate',
                'placeholder': 'First name'
            }),
            'middle_name': TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Middle name'
            }),
            'last_name': TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Last name'
            }),
            'email': TextInput(attrs={
                'class': 'validate',
                'type': 'email'
            }),
            'password': TextInput(attrs={
                'class': 'validate',
                'type': 'password'
            })
        }
