from decimal import Clamped
from os import CLD_CONTINUED
from django.contrib import admin
from .models import Customer,Wallet,Currency,Reward,Receipts,Transaction,ThirdParty,Card,Loan,Notifications
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address",)
    search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("receipt_type","receipt_date", "recipt_number")
    search_fields = ("recipt_number","receipt_date")
admin.site.register(Receipts, ReceiptAdmin)
 
class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_date","transaction_amount","transaction_type")
    search_fields=("transaction_type","transaction_amount")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_type","card_name","cvv_security")
    search_fields=(" date_Issued","card_name")
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("name","phone_Number","thirdparty_id")
    search_fields=("name"," currency")
admin.site.register(ThirdParty,ThirdpartyAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("amount","country_of_origin")
    search_fields=("country_of_origin","amount")
admin.site.register(Currency,CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("date","amount","balance")
    search_fields=("date","amount")
admin.site.register(Wallet,WalletAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("date","customer","gender")
    search_fields=("gender","customer")
admin.site.register(Reward,RewardAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_term",)
    search_fields=("loan_term","guaranter")
admin.site.register(Loan,LoanAdmin) 

class NotificationAdmin(admin.ModelAdmin):
    list_display=("status","date","recipient")
    search_fields=("status","date")
admin.site.register(Notifications,NotificationAdmin)




# Register your models here.


