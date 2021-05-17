from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ["id","author","title","category","create_at"]
    list_display_links= ["id","author","title",]
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name","prep_time","post"]


admin.site.register(Category,MPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Comment)