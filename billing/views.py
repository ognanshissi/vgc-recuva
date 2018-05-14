from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, View, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
import datetime
from .models import Billing
from order.models import Order


class BillingListView(ListView):

    template_name = 'billing/billing_list.html'

    def get_queryset(self):
        qs = Order.objects.all().exclude(status__iexact='paid')
        return qs

    def get_context_data(self, **kwargs):
        ctxt = super(BillingListView, self).get_context_data(**kwargs)
        # print(ctxt['object_list'])
        return ctxt


class UpdateBillingView(View):
    """
    Update bill , making it as paid
    """

    # template_name = 'billing/billing_update_form.html'

    def get(self, request, *args, **kwargs):
        bill_id = kwargs.get('pk')
        order_id = kwargs.get('order_id')
        order_ = get_object_or_404(Order, order_id=order_id)
        bill = get_object_or_404(Billing, pk=bill_id)
        today = datetime.date.today()
        bill.paid_done(today)

        messages.add_message(request, messages.SUCCESS, 'Versement payé')
        redirect_url = reverse_lazy('order:order-detail', kwargs={'order_id': order_id})
        return redirect(redirect_url)

    # def post(self, request, *args, **kwargs):


class CancelBillPaidView(View):

    def post(self, request, *args, **kwargs):
        return redirect(url)

