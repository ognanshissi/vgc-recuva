from django.shortcuts import render
from django.views.generic import View
from django.db.models import Sum
import datetime
from  order.models import Order
from customer.models import Group


class AnalyticsHomeView(View):
    template_name = 'analytics/index.html'

    def get(self, request):
        credit = []
        list = Group.objects.all()
        for g in list:
            total = Order.objects.filter(commercial_group=g).aggregate(Sum('rest'))
            data = {'name': g.name, 'credit': total['rest__sum']}
            credit.append(data)

        MONTHS = (
            (1, 'Janvier'),
            (2, 'Fevrier'),
            (3, 'Mars'),
            (4, 'Avril'),
            (5, 'Mai'),
            (6, 'Juin'),
            (7, 'Juillet'),
            (8, 'Aout'),
            (9, 'Septembre'),
            (10, 'Octobre'),
            (11, 'Novembre'),
            (12, 'Decembre'),
        )
        current = datetime.date.today().month
        ctxt = {
            'months': MONTHS,
            'current': current,
            'data': credit
        }
        return render(request, self.template_name, ctxt)
