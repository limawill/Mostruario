from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import Group
from django.db.models.base import Model
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)
admin.site.site_header = "Admin Mostruario"
admin.site.unregister(Photo)


@admin.register(Photo)  # Nome do model
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("get_photo", "__str__")

    # Django 3.2+
    @admin.display(description="Nome")
    def get_photo(self, obj):
        if obj.image:
            return obj.image.name

    # def has_add_permission(self, request, obj=None):
    #    return False
