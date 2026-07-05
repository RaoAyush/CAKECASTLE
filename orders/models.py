from django.db import models
from bakery.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('baking', 'Baking'),
        ('ready','Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES,default='pickup')
    address=models.TextField(blank=True)
    
    needed_by_date = models.DateField()
    message_on_cake = models.CharField(max_length=100, blank=True)
    special_instruction=models.TextField(blank=True)
    reference_image=models.ImageField(upload_to='order_refs/',blank=True, null=True)

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
    

class OrderItem(models.Model):

    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity=models.PositiveIntegerField(default=1)
    size=models.CharField(max_length=50, blank=True)
    flavour=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.quantity} X {self.product}"