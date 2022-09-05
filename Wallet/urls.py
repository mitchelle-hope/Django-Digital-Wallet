from django.urls import path
from.views import register_Customer

urlpatterns =[ 
    path("register/", register_Customer, name="registration"),
]