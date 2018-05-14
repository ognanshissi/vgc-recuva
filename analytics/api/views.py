import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from billing.models import Billing
from order.models import Order
from customer.models import Group


class AnalyticsView(APIView):

    def get(self, request, format=None):

        req = request.GET.get('month', None)
        n_ = datetime.date.today()
        m_ = n_.month
        if req is None:
            mon = m_
        else:
            mon = req

        groups = Group.objects.all()
        data_ = []
        label_ = []
        dette_total = []
        for gr in groups:
            label_.append(gr.name)
            # total = 0
            total_rest = 0
            bs = 0

            orders = Order.objects.filter(commercial_group=gr)
            for x in orders:
                total_rest += x.rest
                # print(x.ordered_at.month)
                # if x.ordered_at.month == mon:
                    # print(mon)
                    # dette_total += x.advance
                for i in x.billing_set.filter(payment_due__month=mon).exclude(status__iexact='Paid'):
                    bs += i.amount_due
            data_.append(bs)
            dette_total.append(total_rest)

        # qs = Billing.objects.filter(order__commercial_group=g, payment_due__month=month)
        #
        # pending_ = qs.filter(status__iexact='Pending').count()
        # paid_ = qs.filter(status__iexact='Paid').count()
        # late_ = qs.filter(status__iexact='Late').count()
        data = {
            'label': label_,
            'dataSet': data_,
            'rest': dette_total
        }
        return Response(data)


class AnalyticsBillingView(APIView):

    def get(self, request, format=None):
        list = Order.objects.values().all()
        data = {
            'data': list
        }
        return Response(data)
