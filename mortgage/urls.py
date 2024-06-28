from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.mortgage_view, name="mortgage"
    ),  # Ensure 'views.mortgage_view' is a valid view
]
