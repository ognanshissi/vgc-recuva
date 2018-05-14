from django import forms
from .models import Type, Product


class TypeForm(forms.ModelForm):
    name = forms.CharField(label='Type de lentille', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Entrez un type de lentille'
    }))

    code = forms.CharField(label='Code de la lentille', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Type
        fields = ['name', 'code']


class ProductForm(forms.ModelForm):

    AXE_CHOICES = Product.AXE_CHOICES

    qs = Type.objects.all()
    type = forms.ModelChoiceField(queryset=qs, empty_label='Choisissez le type de lentille')
    sphere = forms.DecimalField(label='sphere', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    cylindre = forms.DecimalField(label='cylindre', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    axe = forms.ChoiceField(label='axe', required=False, choices=AXE_CHOICES, widget=forms.NullBooleanSelect(attrs={
        'class': 'form-control'
    }))

    addition = forms.IntegerField(label='Addition', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Product
        fields = ['type', 'sphere', 'cylindre', 'axe', 'addition']

    # def clean(self):
    #     sphere = self.cleaned_data.get('sphere')
    #     cylindre = self.cleaned_data.get('cylindre')
    #     axe = self.cleaned_data.get('axe')
    #     addition = self.cleaned_data.get('addition')