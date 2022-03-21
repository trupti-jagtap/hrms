from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login_function,name="login"),
    path("dashboard/",views.dashboardview,name="dashboard"),
    path("signup/",views.register,name="signup"),
    
]
