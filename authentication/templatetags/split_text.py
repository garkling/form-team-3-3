from django import template


register = template.Library()


@register.filter(name='split_text')
def split_text(text: str) -> list:
    return text.split('.')
