from django.shortcuts import render
from django.http import HttpResponse
from . import admin

# Create your views here.
def index(request):
    data_dict = {"page_title": "About", "app_name": "landing_page"}
    return render(request, 'landing_page/index.html', data_dict)

def signup(request):
    form = admin.UserCreationForm()
    data_dict = {"form":form, "page_title": "Sign Up", "app_name": "landing_page"}
    return render(request, 'landing_page/signup.html', data_dict)
