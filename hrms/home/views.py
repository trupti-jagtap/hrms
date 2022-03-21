from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.shortcuts import render  

from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm

 
# Create your views here.
def home(request):
    return render(request,"home.html")

def login_function(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "login.html" ,{
                "message": "Invalid Credentials, please try again with correct details."
            })

    return render(request, "login.html")


def dashboardview(request):
    return render(request,"dashboard.html")



# Create your views here.  
  
def register(request):  
    if request.POST == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            
    else:  
        form = UserCreationForm()  
   
    return render(request, 'signup.html', {'form':form})  

