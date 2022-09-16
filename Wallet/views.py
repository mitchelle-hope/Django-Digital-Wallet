from django.shortcuts import render
from .models import Account, Card, Currency, Customer, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptsRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

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
    return render(request,"customers_list.html",{"customers":customers})



def register_Currency(request):
    if request.method == "POST":
     form=CustomerRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request,"currency.html",
     {"form": form })
def list_currencys(request):
    currencys= Currency.objects.all()
    return render (request, "currencys_list.html", {"currencys": currencys})



def register_Wallet(request):
    if request.method=="POST":
     form=WalletRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet.html",
     {"form": form })
def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request,"wallets_list.html",{"wallets":wallets})

def register_Account(request):
    if request.method=="POST":
     form=AccountRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"account.html",
     {"form": form })
def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,"accounts_list.html",{"accounts":accounts})


def register_Transaction(request):
    if request.method=="POST":
     form=TransactionRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"transaction.html",
     {"form": form })
def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request,"transactions_list.html",{"transactions":transactions})


def register_Card(request):
    if request.method=="POST":
     form=CardRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"card.html",
     {"form": form })
def list_cards(request):
    cards=Card.objects.all()
    return render(request,"cards_list.html",{"cards":cards})









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

                 
                    
    
