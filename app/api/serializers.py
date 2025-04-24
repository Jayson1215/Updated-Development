from rest_framework import serializers
from .product_models import Product
from .models import Cart, CartItem, Contact

# Product Serializer (from product_models)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Or specify the fields explicitly

# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'updated_at']

# CartItem Serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nesting the Product serializer to show product details
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']

# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
