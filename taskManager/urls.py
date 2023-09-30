from django.urls import path
from . import views

urlpatterns = [
    path('credentials',views.credentials,name="credentials"),
    path('adminLogin',views.adminLogin,name="adminLogin"),
    path('adminSignUp',views.adminSignUp,name="adminSignUp"),
    path('userLogin',views.userLogin,name="userLogin"),
    path('userSignUp',views.userSignUp,name="userSignUp"),
    path('userHomePage',views.userHomePage,name="userHomePage"),
    path('addSprint',views.addSprint,name="addSprint"),
    path('editItem/<str:sprintName>',views.editItem,name="editItem"),
    path('taskBoard/<str:sprintName>',views.taskBoard,name="taskBoard"),
    path('addSprintTask/<str:sprintName>',views.addSprintTask,name="addSprintTask"),
]