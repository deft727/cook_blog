from django import template
from cooksite.models import Category,Post

register = template.Library()

@register.inclusion_tag('include/tags/top_menu.html')
def get_categories():
    categories = Category.objects.all()
    return {"list_category":categories}


@register.inclusion_tag('include/tags/recept_tag.html')
def get_last_posts():
    post = Post.objects.select_related('category').order_by("-id")[:5]
    return {"last_post":post}