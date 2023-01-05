from django.contrib import admin
from .models import Menu, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Category)
admin.site.register(Menu)
