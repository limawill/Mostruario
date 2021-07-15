from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth.models import Group
from django.db.models.base import Model
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Photo)
admin.site.site_header = 'Admin Mostruario'
#
#@admin.register(Model)
#class ModelAdmin(admin.ModelAdmin):
#    list_display = ('__str__', 'get_photo')
#    
#def get_photo(self, obj):
#    if obj.photo:
#        return obj.photo.name