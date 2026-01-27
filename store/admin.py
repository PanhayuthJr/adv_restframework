from django.contrib import admin
from .models import Category, Product, CartItem, WishlistItem, Order, OrderItem

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
    fields = ('name', 'description', 'price', 'category', 'image', 'stock')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('first_name', 'email', 'phone')
    inlines = [OrderItemInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem)
admin.site.register(WishlistItem)