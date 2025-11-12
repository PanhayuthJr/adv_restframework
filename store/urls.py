from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Frontend
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Cart & Wishlist
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),

    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    # =========================
    # Admin Dashboard & CRUD
    # =========================
    # Admin dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),  # make sure this exists
    # Cart & Checkout
    path('checkout_selected/', views.checkout_selected, name='checkout_selected'),

    path('checkout/', views.checkout, name='checkout'),
    # Products CRUD
    path('dashboard/products/', views.product_list, name='product_list'),
    path('dashboard/products/create/', views.product_create, name='product_create'),
    path('dashboard/products/update/<int:pk>/', views.product_update, name='product_update'),
    path('dashboard/products/delete/<int:pk>/', views.product_delete, name='product_delete'),

    # Categories CRUD
    path('dashboard/categories/', views.category_list, name='category_list'),
    path('dashboard/categories/create/', views.category_create, name='category_create'),
    path('dashboard/categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('dashboard/categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

]
