from django.forms import TextInput, Select, \
    CheckboxInput, CharField, ModelForm, Form, PasswordInput, EmailInput, ValidationError
from .models import CustomUser


class CreationUserForm(ModelForm):

    password1 = CharField(widget=PasswordInput)
    password2 = CharField(widget=PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password2 != password1:
            raise ValidationError('Passwords don`t match')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.get_by_email(email):
            raise ValidationError('User is already exists')

        return email

    def save(self, commit=True):
        user = super(CreationUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()

        return user

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'email',
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
            'email': EmailInput()
        }


class UserLoginForm(Form):
    email = CharField(widget=EmailInput)
    password = CharField(widget=PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.get_by_email(email):
            raise ValidationError('This email is not registered')

        return email


class AdminUserForm(ModelForm):

    class Meta:
        model = CustomUser
        exclude = ['uuid']
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
            'password': TextInput(attrs={
                'class': 'validate',
                'type': 'password'
            }),
            'email': EmailInput(),
            'is_active': CheckboxInput(),
            'role': Select()
        }

