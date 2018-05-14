from django import forms
import datetime
from django.shortcuts import get_object_or_404
from .models import Order
from products.models import Type, Product
from customer.models import Group, CustomerProfile, GroupZone


class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Nom et prenom du client',
        widget=forms.TextInput({
            'class': 'form-control'
        })
    )
    contact = forms.CharField(label='Numero de telephone',
                              initial='+225 ',
                              widget=forms.TextInput({
                                  'class': 'form-control'
                              }))
    type = forms.ModelChoiceField(
        label='Type de lentille',
        required=False,
        queryset=Type.objects.all(),
        empty_label='Selectionnez le type de la lentille',
        widget=forms.Select({
            'class': 'form-control'
        })
    )
    detail = forms.CharField(label='Prescription', required=False, widget=forms.Textarea({
        'class': 'form-control',
        'rows': 3
    }))
    commercial_group = forms.ModelChoiceField(
        label='Groupe',
        queryset=Group.objects.all(),
        required=False,
        empty_label='Selectionnez le groupe de prospection', widget=forms.Select({
            'class': 'form-control'
        }))

    zone = forms.IntegerField(label='Zone de prospection',  widget=forms.Select({
        'class': 'form-control'
    }))

    mount = forms.ChoiceField(label='Monture', choices=Order.MOUNT_CHOICES, widget=forms.Select({
        'class': 'form-control'
    }))

    price = forms.IntegerField(initial=40000, label='Prix du verre', widget=forms.TextInput({
        'class': 'form-control'
    }))

    advance = forms.IntegerField(initial=5000, label='Avance', widget=forms.TextInput({
        'class': 'form-control'
    }))

    ordered_at = forms.DateField(label='Date de consultation', widget=forms.DateInput({
        'class': 'form-control',
    }))

    class Meta:
        model = Order
        fields = ['full_name', 'contact', 'commercial_group', 'zone', 'type', 'detail', 'mount', 'price', 'advance', 'ordered_at']

    def clean_zone(self):
        zone = self.cleaned_data.get('zone')
        instance = get_object_or_404(GroupZone, pk=zone)
        if instance is None:
            raise forms.ValidationError('Zone incorrect')
        print(instance)
        return instance

    # def clean_ordered_at(self):
    #     date = self.cleaned_data.get('ordered_at')
    #     print(date)
    #     t = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
    #     return t
