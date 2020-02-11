from django.contrib import admin
from .models import Order, OrderLineItem


# Need to better understand why he added classes here for the admin function
# according to a note that popped up on the screen:
# "The admin interface has the ability to edit more than one model on a single page. This is known as inlines."

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)


admin.site.register(Order, OrderAdmin)
