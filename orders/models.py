from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="orders")
    order_type = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="₽")
    status = models.CharField(max_length=50)
    external_order_id = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.pk}"