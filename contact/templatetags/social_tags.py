from django import template
from contact.models import Social, About


register = template.Library()

# повертає інформацію в обране місце шаблону
@register.simple_tag()
def get_social_links():
    """ вивід усіх посилань соцмереж"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """ вивід про нас"""
    return About.objects.last()

