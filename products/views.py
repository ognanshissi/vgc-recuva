from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Type, Product
from .forms import TypeForm, ProductForm


class TypeListView(ListView):

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(CreateView):
    model = Type
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('product:type-list')
    form_class = TypeForm  # One of both should stay "form_class or fields"
    # fields = ['name', 'code']


class TypeUpdateView(UpdateView):
    model = Type
    success_url = reverse_lazy('product:type-list')
    template_name_suffix = '_update_form'
    form_class = TypeForm

    def get_context_data(self, **kwargs):
        context = super(TypeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'This is a title'
        return context


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        ctxt = super(ProductListView, self).get_context_data(**kwargs)
        types = Type.objects.all()
        # lens_type_list = [value for key, value in types]
        ctxt['types'] = types
        print(ctxt)
        return ctxt

    def get_queryset(self):
        lens_type = self.request.GET.get('lens_type')

        if lens_type and lens_type != 'tous':
            qs = Product.objects.filter(type__code__iexact=lens_type)
        else:
            qs = Product.objects.all()
        return qs


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('product:product-list')
    form_class = ProductForm
    template_name_suffix = '_create_form'


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy('product:product-list')
    form_class = ProductForm
    template_name_suffix = '_update_form'

