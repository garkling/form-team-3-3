from django import forms

from .models import CustomUser


class CreationUserForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password2 != password1:
            raise forms.ValidationError('Passwords don`t match')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.get_by_email(email):
            raise forms.ValidationError('User is already exists')

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
            'first_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'First name'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Middle name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput()
        }


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        candidate = CustomUser.get_by_email(email)

        if not candidate or not candidate.check_password(password):
            raise forms.ValidationError('Incorrect username or password')

        return cleaned_data


class AdminUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        exclude = ['uuid']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'First name'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Middle name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'validate',
                'placeholder': 'Last name'
            }),
            'password': forms.TextInput(attrs={
                'class': 'validate',
                'type': 'password',
            }),
            'email': forms.EmailInput(),
            'is_active': forms.CheckboxInput(),
            'role': forms.Select()
        }

