from django.contrib import admin
from .models import Billing


class BillingAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_due', 'amount_due', 'paid_at', 'status', 'billing_order')
    list_filter = (
        ('order'),
        ('status')
    )


admin.site.register(Billing, BillingAdmin)
