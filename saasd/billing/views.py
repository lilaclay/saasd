# import stripe
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse


@Login_required
def billing_home(request: HttpRequest):
    return render(request, "billing/billing_home.html")

@Login_required
def checkout_session(request: HttpRequest):
    if request.method == "POST":
        # stripe.api_key = settings.STRIPE_API_KEY
        # if request.user.stripe_customer_id:
        # pass
        # customer_id = request.user.stripe_customer_id
        # else:
        # customer = stripe.Customer.create(
        #     email=request.user.email,
        # )
        # customer_id = customer["id"]
        # request.user.save()
        # session = stripe.checkout.Session.create(
        #     payment_method_types=['card'],
        #     mode='setup',
        #     customer='cus_L4Y2v5Zc9Z5VhP',
        #     success_url=request.build_absolute_url(reverse('billing:checkout_success')) + '?session_id={CHECKOUT_SESSION_ID}',
        #     cancel_url='http://localhost:4242/cancel',
        # )

        # return redirect(session.url, code=303)
        pass
    else:
        return render(request, "billing/checkout_session.html")

@Login_required
def checkout_success(request: HttpRequest):
    # session_id = request.GET.get("session_id")
    # stripe.api_key = settings.STRIPE_API_KEY
    # session = stripe.checkout.Session.retrieve(session_id)
    return render(request, "billing/checkout_success.html")
