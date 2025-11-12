from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'image')
    search_fields = ('name', 'description')
    list_filter = ('category', 'price', 'stock')
    ordering = ('name',)
    fields = ('name', 'description', 'price', 'category', 'image', 'stock')  # Customize form fields

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)