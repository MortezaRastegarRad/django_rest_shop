from django.contrib import admin

from .model.models import Entity, Order


admin.site.register(Entity)
admin.site.register(Order)
