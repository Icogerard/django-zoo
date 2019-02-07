from django.contrib import admin
from .models import Category, Animal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'extinct', 'created', 'updated']
    list_filter = ['extinct', 'created', 'updated']
    list_editable = ['extinct']
    prepopulated_fields = {'slug': ('name',)}


    
