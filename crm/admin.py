from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

# Register your models here.
class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_dt','coment_text')
    readonly_fields = ('coment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    #поле класса комент
    inlines = [Coment,]




admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
