from django.contrib import admin
from .models import Order
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "order_type", "status", "total_amount", "created_at"]
    list_filter = ["status", "order_type"]
    search_fields = ["user__email", "external_order_id"]
    readonly_fields = ["created_at", "updated_at"]