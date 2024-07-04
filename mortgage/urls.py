from django.urls import path
from . import views

urlpatterns = [
    path(
        "mortage_payment_calculator/",
        views.mortgage_calculator_view,
        name="mortgage_payment",
    ),
]
