from django.contrib import admin
from .models import CustomerProfile, Group, GroupZone


admin.site.register(Group)
admin.site.register(CustomerProfile)
admin.site.register(GroupZone)

# Register your models here.
