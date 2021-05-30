from django.contrib import admin
from .models import *



@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","created_at"]
    list_display_links = ["name"]


class ImageAboutInlines(admin.StackedInline):
    model = ImageAbout
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInlines]

admin.site.register(ContactLink)
admin.site.register(Social)
# admin.site.register(ImageAbout)

