from django.contrib import admin
from .models import Category

admin.site.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     search_fields = ['category']
#     autocomplete_fields = ['parent']
#     list_filter = ['parent']