from django.urls import path
from.views import list_customers, register_Account, register_Card, register_Currency, register_Customer, register_Loan, register_Notifications, register_Receipts, register_Reward, register_ThirdParty, register_Transaction, register_Wallet

urlpatterns =[ 
    path("register/", register_Customer, name="registration"),
    path("currency/", register_Currency, name="currency"),
    path("wallet/", register_Wallet, name="wallet"),
    path("account/", register_Account, name="account"),
    path("transaction/", register_Transaction, name="transaction"),
    path("card/", register_Card, name="card"),
    path("thirdParty/", register_ThirdParty, name="thirdparty"),
    path("notifications/", register_Notifications, name="notifications"),
    path("receipts/", register_Receipts, name="receipts"),
    path("loan/", register_Loan, name="loan"),
    path("reward/", register_Reward, name="reward"),
    path("customers/",list_customers,name="customers_list"),
]

