from django.urls import path
from . import views

urlpatterns = [
    path('credentials',views.credentials,name="credentials"),
]