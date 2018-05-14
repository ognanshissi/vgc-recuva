from django.db import models
import datetime
from order.models import Order
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save


class Billing(models.Model):
    now = datetime.datetime.today()
    STATUS_CHOICES = (
        ('Paid', 'Soldé'),
        ('Late', 'Retard'),
        ('Pending', 'En Attente')
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    payment_due = models.DateField(auto_now=False)
    amount_due = models.DecimalField(default=2500.00, decimal_places=2, max_digits=1000)
    paid_at = models.DateField(auto_now=False, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    billing_order = models.PositiveSmallIntegerField(default=1, editable=False)

    def __str__(self):
        return 'Versement numéro {}'.format(self.billing_order)

    class Meta:
        ordering = ['pk']

    def get_paid_at_display(self):
        if self.paid_at:
            return self.paid_at
        else:
            return 'N/A'

    def get_billing_update_url(self):
        if self.status == 'Late' or self.status == 'Pending':
            return reverse('order:order-billing-update', kwargs={
                'order_id': self.order.order_id,
                'pk': self.pk
            })
        else:
            return ''

    def get_display_name(self):
        return 'vers {}'.format(self.billing_order)

    def paid_done(self, paid_at):
        self.status = 'Paid'
        cost = self.amount_due
        # self.amount_due = 0.00
        self.paid_at = paid_at

        self.save()
        # print(paid_at)
        # print(self.paid_at)
        order_ = self.order
        # print(order_)
        rest = int(order_.rest) - int(cost)
        order_.rest = rest
        if rest == 0.0:
            order_.status = 'paid'
        order_.save()
        return self.status

    def make_late(self):
        if self.payment_due >= self.now:
            self.status = 'Late',
            self.save()
        return self.status


def post_save_update_billing(sender, instance, created, *args, **kwargs):
    if created and instance.paid_at:
        today = datetime.date.today()
        instance.paid_done(today)


post_save.connect(post_save_update_billing, sender=Billing)
