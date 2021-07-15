from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import Group
from django.db.models.base import Model
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)
admin.site.site_header = 'Admin Mostruario'

@admin.register(Photo)  # Nome do model
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_photo')

    # Identação
    # def get_photo(self, obj):
    #     if obj.image:
    #         return obj.image.name

    # Antes do Django 3.2
    # get_photo.short_description = 'Foto'

    # Django 3.2+
    @admin.display(description='Foto')
    def get_photo(self, obj):
        if obj.image:
            return obj.image.name