from django import template
from mysite.docgurnal.models import *

register = template.Library()



@register.filter(name='addclassrow')
def addclassrow(field, class_attr):
    rowcol = '3'
    return field.as_widget(attrs={'class': class_attr, 'rows': rowcol })

@register.filter(name='addclassrowdva')
def addclassrowdva(field, class_attr, rowcol):
    # rowcol = '3'
    return field.as_widget(attrs={'class': class_attr, 'rows': rowcol })

@register.filter(name='eremfortext')
def eremfortext(eremfield):
    return "Да" if eremfield else "Нет"

@register.filter(name='nonefortext')
def nonefortext(fieldvalue):
    return fieldvalue if fieldvalue and fieldvalue != "NULL" and fieldvalue != "None" and fieldvalue != ""  else "Не указано"

@register.filter(name='noneforempty')
def noneforempty(fieldvalue):
    return fieldvalue if fieldvalue and fieldvalue != "NULL" and fieldvalue != "None" and fieldvalue != ""  else ""


@register.simple_tag
def field_name(value, field):
    '''
    Django template filter which returns the verbose name of an object's,
    model's or related manager's field.
    '''
    if hasattr(value, 'model'):
        value = value.model
    return value._meta.get_field(field).verbose_name


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name



@register.simple_tag
def my_save():
    return "Сохранить"

@register.simple_tag
def my_notsave():
    return "Выйти без сохранения"


@register.simple_tag
def my_comeback():
    return "Обратно к списку"


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    return obj._meta.verbose_name_plural