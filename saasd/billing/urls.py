from django.urls import path
from saasd.billing.views import billing_home

app_name = "billing"
urlpatterns = [
    path("", view=billing_home, name="home"),
]
