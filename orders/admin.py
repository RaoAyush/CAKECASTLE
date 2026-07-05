from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name','phone','status','needed_by_date','created_at')
    list_filter=('status','delivery_type')
    inline = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

# Register your models here.
