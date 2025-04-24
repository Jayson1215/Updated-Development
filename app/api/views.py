from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, Product, Cart, CartItem  # Import the Cart and CartItem models
from .serializers import ProductSerializer  # Make sure to create a ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated  # Ensure the user is authenticated
from .product_models import Product

# Example of an existing view
def contact_view(request):
    return HttpResponse('Contact Page')

# HelloWorld view
class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

# Students view
class Students(APIView):
    def get(self, request):
        students = {
            1: {
                "student_id": "12345",
                "name": "Alice Johnson",
                "program": "Computer Science",
                "year_level": "Sophomore"
            },
            2: {
                "student_id": "S23456",
                "name": "Bob Smith",
                "program": "Mechanical Engineering",
                "year_level": "Junior"
            },
            3: {
                "student_id": "S34567",
                "name": "Charlie Brown",
                "program": "Business Administration",
                "year_level": "Senior"
            },
            4: {
                "student_id": "S45678",
                "name": "Diana Green",
                "program": "Electrical Engineering",
                "year_level": "Freshman"
            }
        }
        return Response(students, status=status.HTTP_200_OK)

# ContactListView for adding contact
class ContactListView(APIView):
    def create_contact(self, data):
        return Contact(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone_number=data.get('phone_number', ''),
            address=data.get('address', '')
        )

    def post(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, dict):  # Single entry
            contact = self.create_contact(data)
            contact.save()
            return Response({"message": "Contact added successfully!", "id": contact.id}, status=status.HTTP_201_CREATED)
        elif isinstance(data, list):  # Bulk upload
            contacts = [self.create_contact(item) for item in data]
            Contact.objects.bulk_create(contacts)
            return Response({"message": f"{len(contacts)} contacts added successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST)

# ProductListCreateView for handling products
class ProductListCreateView(APIView):
    def get(self, request):
        # Fetch all products from the database
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new product from the POST data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CartView for managing the user's cart
class CartView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        """ Add a product to the cart """
        user = request.user  # Get the current authenticated user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        # Fetch the product from the database
        product = get_object_or_404(Product, id=product_id)

        # Check if the user already has a cart, else create one
        cart, created = Cart.objects.get_or_create(user=user)

        # Check if the product already exists in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # If the item already exists, update the quantity
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return Response({"message": "Product added to cart successfully!"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        """ View the user's cart and the items in it """
        user = request.user
        cart = Cart.objects.filter(user=user).first()

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            cart_data = []
            for item in cart_items:
                cart_data.append({
                    "product_name": item.product.name,
                    "quantity": item.quantity,
                    "price": item.product.price,
                })
            return Response(cart_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Your cart is empty."}, status=status.HTTP_404_NOT_FOUND)
