from django.shortcuts import render
from .forms import CustomerRegistrationForm

# Create your views here.

def register_Customer(request):
    form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",
     {"form": form })

     
