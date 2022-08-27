from django.contrib import admin

# Register your models here.
from ecomerce_app1.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'colors', 'grade', 'rating', 'quality', 'created_by']


admin.site.register(Products, ProductAdmin)
