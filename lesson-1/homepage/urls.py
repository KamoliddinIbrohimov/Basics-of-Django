from django.urls import path
from .views import homePageViews

urlpatterns = [
    path('', homePageViews, name='home')
    ]