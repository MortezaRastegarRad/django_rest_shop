from django.contrib import admin
from .api.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'is_published', 'category', 'price', 'description', 'create_at', 'updated_at',
        'images_path', 'options'
    ]
    list_filter = [
        'create_at', 'updated_at', 'category'
    ]
    list_editable = ['price', 'name', 'options']


admin.site.register(Product, ProductAdmin)
