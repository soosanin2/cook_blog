from django import template
from blog.models import Category, Post


register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    """виводить усі категорії"""
    return get_all_categories()


# рендерить шаблон з інформацією
@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = get_list_category()
    return {"list_category": category}


@register.inclusion_tag('blog/include/tags/resires_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return {"list_last_post": posts}


