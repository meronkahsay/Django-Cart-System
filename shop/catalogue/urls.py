from django.urls import path
from . import views
from .views import product_list ,create_product


urlpatterns = [
    path('', product_list, name='product_list'),  
    path('products/', product_list, name='product_list'), 
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_details, name='product_details'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('products/create',create_product,name = 'create_product'),
    path('product/<int:id>/upload-image/', views.upload_product_image, name='upload_product_image'),
]

