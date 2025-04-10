# product_urls.py
from django.urls import path
from .product_views import ProductListView, ProductDetailView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
