from django.urls import path
from . import views

urlpatterns = [
    path('credentials',views.credentials,name="credentials"),
    path('adminLogin',views.adminLogin,name="adminLogin"),
    path('adminSignUp',views.adminSignUp,name="adminSignUp"),
    path('addSprint',views.addSprint,name="addSprint"),
]