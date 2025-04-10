from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # List display: Columns to show in the product list view
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at', 'updated_at')
    
    # Search fields: Fields to search for in the admin search bar
    search_fields = ('name', 'category', 'brand')
    
    # List filter: Filters to show in the sidebar for easy filtering
    list_filter = ('category', 'brand')
    
    # Optional: You can add additional features like ordering and pagination
    ordering = ('name',)  # Order the products by name
    list_per_page = 25  # Limit the number of products per page in the admin list view
    
    # Optional: Fieldsets can be used to organize form layout in the admin interface
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'description', 'stock_quantity', 'brand', 'supplier', 'warranty_period', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Optional: Add a collapsible class to the timestamps section
        }),
    )
    
    # Optional: You can make some fields read-only if needed
    readonly_fields = ('created_at', 'updated_at')
