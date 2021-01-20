from django import template

register = template.Library()


@register.simple_tag
def convert_date(date):
    if date:
        return date.strftime('%Y-%m-%d %H:%M:%S')

    return None
