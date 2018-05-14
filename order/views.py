import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, RedirectView, View, CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from billing.models import Billing
from .models import Order
from .forms import OrderCreateForm


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.all()


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name_suffix = '_create_form'
    # success_url = reverse_lazy('order:order-')


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        ctxt = super(OrderDetailView, self).get_context_data(**kwargs)
        obj = kwargs.get('object')
        obj.update_billing_payment_due()
        for b in obj.billing_set.filter(status__iexact='Pending'):
            if b.payment_due < today:
                b.status = 'Late'
                b.save()
        return ctxt

    def get_object(self, queryset=None):
        order_id = self.kwargs.get('order_id')
        obj = get_object_or_404(Order, order_id=order_id)

        # obj.update()
        return obj


class DeliveredOrderView(View):
    """
    Process the delivery of the order and generate all billings by setting the first bill to paid
    """
    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: nothing
        """
        redirect_url = reverse('order:order-detail', kwargs={'order_id': kwargs.get('order_id')})
        delivery_date = request.POST.get('delivery', None)
        if delivery_date:
            deliver_at = datetime.datetime.strptime(delivery_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        else:
            deliver_at = datetime.datetime.today()

        order_id = kwargs.get('order_id')
        order_ = get_object_or_404(Order, order_id=order_id)
        order_.status = 'shipped'
        order_.shipped = True
        order_.shipped_at = datetime.datetime.strptime(deliver_at, '%Y-%m-%d')
        order_.save()
        for i in range(1, int(order_.billing_count + 1)):
            if i == 1:
                vers1 = Billing.objects.create(
                    order=order_,
                    payment_due=(order_.shipped_at + datetime.timedelta(weeks=i-1)),
                    amount_due=2500.00,
                    # paid_at=order_.shipped_at,
                    billing_order=i
                )
                vers1.paid_done(order_.shipped_at)
            else:
                Billing.objects.create(
                    order=order_,
                    payment_due=(order_.shipped_at + datetime.timedelta(weeks=i-1)),
                    amount_due=2500.00,
                    billing_order=i
                )
        messages.add_message(request, messages.SUCCESS, 'Livraison de la commande est  validée')
        return redirect(redirect_url)


class CancelDeliveredOrderView(View):

    def post(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = get_object_or_404(Order, order_id=order_id)
        if order.shipped:
            for b in order.billing_set.all():
                if b.status == 'Paid':
                    order.rest += b.amount_due
                b.delete()
            order.status = 'created'
            order.shipped = False
            order.shipped_at = None
            order.save()
            messages.add_message(request, messages.SUCCESS, 'La livraison de la commande a bien été annullée')

        redirect_url = order.get_absolute_url()

        return redirect(redirect_url)


class CompletePaymentView(View):

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get('order_id')
        redirect_url = reverse('order:order-detail', kwargs={'order_id': kwargs.get('order_id')})

        # grab remain billing not yet completed
        order = get_object_or_404(Order, pk=order_id)
        billings = order.billing_set.all().exclude(status='Paid')

        for b in billings:
            today = datetime.date.today()
            b.paid_done(today)

        messages.add_message(request, messages.SUCCESS, 'La commande a été complètement soldé')
        return redirect(redirect_url)
