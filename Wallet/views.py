from django.shortcuts import render
from .models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptsRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.

def register_Customer(request):
    if request.method=="POST":
        form=(CustomerRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_customer.html",
     {"form": form })

def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})



def register_Currency(request):
    form=CustomerRegistrationForm()
    return render(request,"currency.html",
     {"form": form })

def register_Wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet.html",
     {"form": form })

def register_Account(request):
    form=AccountRegistrationForm()
    return render(request,"account.html",
     {"form": form })

def register_Transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"transaction.html",
     {"form": form })

def register_Card(request):
    form=CardRegistrationForm()
    return render(request,"card.html",
     {"form": form })



def register_ThirdParty(request):
    form=ThirdPartyRegistrationForm()
    return render(request,"thirdparty.html",
     {"form": form })


def register_Notifications(request):
    form=NotificationsRegistrationForm()
    return render(request,"notifications.html",
     {"form": form })


def register_Receipts(request):
    form=ReceiptsRegistrationForm()
    return render(request,"receipts.html",
     {"form": form })


def register_Loan(request):
    form=LoanRegistrationForm()
    return render(request,"loan.html",
     {"form": form })


def register_Reward(request):
    form=RewardRegistrationForm()
    return render(request,"reward.html",
     {"form": form })

                 
                    
    
