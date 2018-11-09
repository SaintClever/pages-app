from django.urls import path
from .views import HomePageView, AboutPageView # imported from views.py

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]