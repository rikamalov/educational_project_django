from django.contrib import admin
from .models import PriceCard, PriceTable

# Register your models here.
admin.site.register(PriceTable)
admin.site.register(PriceCard)
