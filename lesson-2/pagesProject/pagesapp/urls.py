from django.urls import path
from .views import HomePageView, AboutPageView, MynamePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('my name', MynamePageView.as_view(), name='my name'),
]