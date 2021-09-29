from django import template

register = template.Library()

#@register.filter(name='cut')
def cut(value, arg):
    """
    Cuts out the values of arg passed as string
    """
    return value.replace(arg, '')

register('cut', cut)
