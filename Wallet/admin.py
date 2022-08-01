from django.contrib import admin
from .models import Customer,Wallet,Currency,Reward,Receipts,Transaction,ThirdParty,Card,Loan,Notifications
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address",)
    search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Receipts)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Reward)
admin.site.register(Loan)
admin.site.register(Notifications)



# Register your models here.


