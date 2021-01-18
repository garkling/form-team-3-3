from django.forms import Form, ChoiceField


class FilterForm(Form):
    OPTIONS = (
        ('3', '3 days'),
        ('5', '5 days'),
        ('7', '1 week'),
        ('30', '1 month'),
    )

    select = ChoiceField(choices=OPTIONS)
