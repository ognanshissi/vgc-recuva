from django.db import models
import datetime
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse_lazy
from customer.models import CustomerProfile
from products.models import Product, Type
from customer.models import Group, GroupZone
from recovery.utils import unique_order_id_generator


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('created', 'Non Livré'),
        ('paid', 'Soldé'),
        ('shipped', 'Livré'),
        ('refunded', 'Recuperé'),
    )

    MOUNT_CHOICES = (
        ('rayban classic', 'RayBan Classic'),
        ('rayban', 'RayBan'),
        ('chat', 'Chat')
    )
    now = datetime.datetime.today()
    order_id = models.CharField(max_length=255, null=True, blank=True, editable=False)  # generate ids like AD012AS
    # customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    commercial_group = models.ForeignKey(Group, on_delete=models.CASCADE, default='1')
    zone = models.ForeignKey(GroupZone, on_delete=models.CASCADE, default='1')
    detail = models.TextField(max_length=255, default='')
    mount = models.CharField(max_length=100, choices=MOUNT_CHOICES, null=True, blank=True, default='rayban classic')
    price = models.DecimalField(max_digits=100, decimal_places=2, default=60000.00)
    advance = models.DecimalField(max_digits=100, default=5000.00, decimal_places=2)
    rest = models.DecimalField(max_digits=100, default=0.00, decimal_places=2)
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='created')
    ordered_at = models.DateField(auto_now=False, null=True, blank=True)
    scheduled_shipped_at = models.DateField(default=None, auto_now=False, null=True, blank=True)
    shipped = models.BooleanField(default=False)
    shipped_at = models.DateField(auto_now=False, default=None, blank=True, null=True)
    number_of_month_complete = models.IntegerField(default=2)
    billing_count = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id

    def complete_paiement_order(self):
        self.rest = 0.0
        self.status = 'paid'
        self.save()

    def payment_status_check(self):
        now = datetime.datetime.today()
        count = self.billing_set.filter(payment_due__lt=now).exclude(status='Paid').count()
        return count

    def get_absolute_url(self):
        return reverse_lazy('order:order-detail', kwargs={'order_id': self.order_id})

    def get_delivered_url(self):
        if self.status == 'created':
            return reverse_lazy('order:order-delivered', kwargs={'order_id': self.order_id})
        else:
            return None

    def get_cancel_order_url(self):
        if self.shipped:
            return reverse_lazy('order:order-cancel', kwargs={'order_id': self.order_id})
        else:
            return None

    def get_complete_order_url(self):
        if self.status != 'paid' or self.status != 'refunded':
            return reverse_lazy('order:order-complete', kwargs={'order_id': self.order_id})
        else:
            return None

    def update_rest(self):
        total_ = (self.price - self.advance)
        # formatted_total = format(total_, '.2f')
        self.rest = total_
        self.save()
        return total_

    # def billing_not_paid_count(self):
    #     count = Billing.objects.filter(order__pk=self.pk).exclude(status='Paid').count()
    #     return count

    def update_shipped_at(self):
        schedule = (self.ordered_at + datetime.timedelta(weeks=2))
        self.scheduled_shipped_at = schedule
        self.save()
        return schedule

    def billing_count_update(self):
        self.update_shipped_at()
        rest = self.update_rest()
        count = rest / 2500
        self.billing_count = count
        self.save()
        return count

    def update_billing_payment_due(self):
        if self.shipped:
            for b in self.billing_set.filter(status__iexact='Paid'):
                if b.amount_due == 0.0:
                    b.amount_due = 2500.0
                    b.save()
            first_bill = self.billing_set.first()
            if first_bill.payment_due != self.shipped_at:
                count = 1
                for bill in self.billing_set.all():
                    bill.payment_due = self.shipped_at + datetime.timedelta(weeks=count - 1)
                    bill.save()
                    count += 1


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.billing_count_update()


post_save.connect(post_save_order, sender=Order)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_receiver, sender=Order)


# def post_save_create_billings(sender, instance, created, *args, **kwargs):
#     if created:
#         for i in range(1, int(instance.billing_count + 1)):
#             Billing.objects.create(
#                 order=instance,
#                 payment_due=(instance.scheduled_shipped_at + datetime.timedelta(weeks=i-1)),
#                 amount_due=2500.00,
#                 billing_order=i
#             )


# post_save.connect(post_save_create_billings, sender=Order)


