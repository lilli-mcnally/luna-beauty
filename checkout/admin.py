from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date', 
        'delivery_cost',
        'order_total',
        'grand_total',
        'discount',
        )

    fields = (
        'order_number',
        'date',
        'first_name',
        'last_name',
        'email',
        'phone',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
        'delivery_cost',
        'order_total',
        'grand_total',
        'discount',
        )

    list_display = (
        'order_number',
        'date',
        'first_name',
        'last_name',
        'email',
        'delivery_cost',
        'order_total',
        'discount',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)