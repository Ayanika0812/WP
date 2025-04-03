# webapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This should route to the home view
]
