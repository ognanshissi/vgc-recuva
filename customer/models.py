from django.db import models
from django.core.urlresolvers import reverse_lazy, reverse


class Group(models.Model):
    CITY_CHOICES = (
        ('abidjan', 'Abidjan'),
        ('bouake', 'Bouaké'),
        ('daloula', 'Daloula')
    )

    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255, choices=CITY_CHOICES, default='abidjan')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer:group-update', kwargs={'pk': self.pk})

    def get_api_create_zone_url(self):
        return reverse('api-customer:zone-create', kwargs={'pk': self.pk})

    def get_absolute_detail_url(self):
        return reverse('customer:group-detail', kwargs={'pk': self.pk})


class GroupZone(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('customer:group-zone-detail', kwargs={'pk': self.group.pk, 'zone_id': self.pk})


class CustomerCategory(models.Model):
    name = models.CharField(max_length=255)


class CustomerProfile(models.Model):

    GENDER_CHOICES = (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),
        ('Mlle', 'Mademoiselle')
    )

    CATEGORY_CHOICES = (
        ('structure', 'Structure'),
        ('particulier', 'Particulier')
    )

    # group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # zone = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='particulier')
    # structure_name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "{gender} {first_name} {last_name}".format(gender=self.gender, last_name=self.last_name, first_name=self.first_name)

    def get_absolute_url(self):
        return reverse('customer:customer-detail', kwargs={'pk': self.pk})