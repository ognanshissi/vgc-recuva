from django import forms
from .models import CustomerProfile, Group, GroupZone


class CustomerProfileCreateForm(forms.ModelForm):

    gender = forms.ChoiceField(label='Genre', choices=CustomerProfile.GENDER_CHOICES, widget=forms.Select({
        'class': 'form-control'
    }))

    first_name = forms.CharField(label='Nom', widget=forms.TextInput({
        'class': 'form-control'
    }))
    last_name = forms.CharField(label='Prenom', widget=forms.TextInput({
        'class': 'form-control'
    }))

    category = forms.ChoiceField(label='Categorie', choices=CustomerProfile.CATEGORY_CHOICES, widget=forms.Select({
        'class': 'form-control'
    }))

    # structure_name = forms.CharField(label='Nom de la structure', required=False, widget=forms.TextInput({
    #     'class': 'form-control',
    #     'placeholder': 'Ex.: Nom de l\'école ...'
    # }))

    contact = forms.IntegerField(label='Numéro de téléphone', widget=forms.TextInput({
        'class': 'form-control'
    }))

    address = forms.CharField(label='Adresse', widget=forms.Textarea({
        'class': 'form-control',
        'rows': 3
    }))

    class Meta:
        model = CustomerProfile

        fields = ['gender', 'first_name', 'last_name', 'category', 'contact', 'address']

    def clean_structure_name(self):
        category = self.cleaned_data.get('category')
        structure_name = self.cleaned_data.get('structure_name')

        if structure_name is None and category == 'structure':
            raise forms.ValidationError('Veuillez saissir la structure du client')

        return structure_name


class GroupCreateForm(forms.ModelForm):

    name = forms.CharField(label='Nom du groupe', widget=forms.TextInput({
        'class': 'form-control'
    }))
    city = forms.ChoiceField(label='Ville', choices=Group.CITY_CHOICES, widget=forms.Select({
        'class': 'form-control'
    }))

    class Meta:
        model = Group
        fields = ['name', 'city']


class GroupZoneCreateForm(forms.Form):
    name = forms.CharField(label="Nom de la zone", widget=forms.TextInput({
        'class': 'form-control'
    }))

