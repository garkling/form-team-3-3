from django import forms

from .models import Book
from author.models import Author


class AuthorMultiplyChoiceField(forms.ModelMultipleChoiceField):

    def clean(self, value):
        if not value:
            raise forms.ValidationError('You need to choose an author(s)')

        cleaned_data = super().clean(value)
        return cleaned_data

    def label_from_instance(self, author):
        return f'{author.name} {author.surname} {author.patronymic}'


class BookCreationForm(forms.ModelForm):

    authors = AuthorMultiplyChoiceField(
        queryset=Author.get_all(),
        widget=forms.SelectMultiple(),
    )

    class Meta:
        model = Book
        exclude = ['uuid']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            }),
            'count': forms.NumberInput(),
        }

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count <= 0:
            raise forms.ValidationError('Invalid count of books')

        return count
