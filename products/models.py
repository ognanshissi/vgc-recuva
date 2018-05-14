from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import reference_generator


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_update_url(self):
        return reverse('product:type-update', kwargs={'pk': self.pk})


class Product(models.Model):
    AXE_CHOICES = (
        (None, 'selectionnez de l\'axe la lentille'),
        ('90', '90°'),
        ('110', '110°'),
        ('180', '180°')
    )
    reference = models.CharField(max_length=255, null=True, blank=True, unique=True)
    # type = models.CharField(max_length=25, choices=LENS_TYPE_CHOICES)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    sphere = models.DecimalField(default=0.00, null=True, blank=True, max_digits=3, decimal_places=2)
    cylindre = models.DecimalField(default=0.00, null=True, blank=True, decimal_places=2, max_digits=3)
    axe = models.CharField(max_length=4, default=None, null=True, blank=True, choices=AXE_CHOICES)
    addition = models.PositiveSmallIntegerField(null=True, blank=True)
    # in_stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return "{}".format(self.reference)

    def get_absolute_url(self):
        pass

    def get_update_url(self):
        return reverse('product:product-update', kwargs={'pk': self.pk})

    @property
    def axe_text(self):
        if self.axe is not None:
            return 'axe: {}°'.format(self.axe)
        else:
            return ''

    @property
    def addition_title(self):
        if self.addition and self.addition > 0:
            return 'ADD + {}'.format(self.addition)
        else:
            return ''


def pre_save_product(sender, instance, *agrs, **kwargs):
    if instance.reference is None:
        instance.reference = reference_generator(instance)


pre_save.connect(pre_save_product, sender=Product)