from django.db import models

class Product(models.Model):
    # Product fields
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
    stock_quantity = models.IntegerField(default=0, verbose_name="Stock Quantity")
    category = models.CharField(max_length=100, verbose_name="Product Category")
    brand = models.CharField(max_length=100, verbose_name="Brand")
    supplier = models.CharField(max_length=100, verbose_name="Supplier")
    warranty_period = models.CharField(max_length=100, verbose_name="Warranty Period", blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Product Image")

    # Timestamps to track product creation and updates
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    # String representation of the model for better readability
    def __str__(self):
        return self.name

    # Adding validation to ensure price is positive and stock is non-negative
    def clean(self):
        if self.price <= 0:
            raise ValueError("Price must be greater than zero.")
        if self.stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

    # Optional: Calculate the total value of the stock (stock_quantity * price)
    def total_stock_value(self):
        return self.stock_quantity * self.price

    # Meta options to customize model behavior
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']  # Optional: you can change the default ordering

