from django.shortcuts import redirect, get_object_or_404
from reportlab.pdfgen import canvas
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, View, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from recovery.mixins import AjaxFormMixin
from .models import CustomerProfile, Group, GroupZone
from .forms import CustomerProfileCreateForm, GroupCreateForm, GroupZoneCreateForm


class CustomerProfileListView(ListView):

    def get_queryset(self):
        return CustomerProfile.objects.all()


class CustomerProfileCreateView(SuccessMessageMixin, CreateView):
    model = CustomerProfile
    form_class = CustomerProfileCreateForm
    success_url = reverse_lazy('customer:customer-list')
    success_message = 'Le client a été ajouté avec succès'
    template_name_suffix = '_create_form'


class CustomerProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = CustomerProfile
    form_class = CustomerProfileCreateForm
    success_url = reverse_lazy('customer:customer-list')
    success_message = 'Client modifié avec succès'
    template_name_suffix = '_update_form'


class GroupCreateView(CreateView):
    model = Group
    template_name_suffix = '_create_form'
    form_class = GroupCreateForm
    success_message = "Le groupe a été ajouté avec succès"


class GroupListView(ListView):

    def get_queryset(self):
        qs = Group.objects.all()
        return qs


class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    template_name_suffix = '_update_form'
    form_class = GroupCreateForm
    success_message = "Le groupe a été modifié avec succès"
    success_url = reverse_lazy('customer:group-list')

    # def post(self, request, *args, **kwargs):
    #     # p = super(GroupUpdateView, self).post(request, *args, **kwargs);
    #     f = GroupZoneForm(request.POST)
    #     g = get_object_or_404(Group, pk=kwargs.get('pk'))
    #     if f.is_valid():
    #         instance = f.save(commit=False)
    #         instance.group = g
    #         instance.save()
    #         messages.add_message(request, messages.SUCCESS, 'La zone a bien ete ajouter')
    #         return redirect(g.get_absolute_url())
    #
    #     return redirect(g.get_absolute_url())

    def get_context_data(self, **kwargs):
        ctxt = super(GroupUpdateView, self).get_context_data(**kwargs)
        # ctxt['zone_form'] = GroupZoneCreateForm
        return ctxt


class GroupDetailView(DetailView):
    model = Group
    template_name_suffix = '_detail'


class GroupZoneDetailView(DetailView):
    model = GroupZone
    template_name_suffix = '_detail'

    def get_object(self, queryset=None):
        # ctxt = super(GroupZoneDetailView, self).get_context_data(kwargs)
        zone_id = self.kwargs.get('zone_id')
        obj = get_object_or_404(GroupZone, pk=zone_id)
        return obj


