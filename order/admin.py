from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
	list_display = ('order_id', 'full_name', 'contact', 'rest', 'status', )


admin.site.register(Order, OrderAdmin)
# Register your models here.
