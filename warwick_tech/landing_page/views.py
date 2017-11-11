from django.shortcuts import render
from django.http import HttpResponse
from . import admin

# Create your views here.
def index(request):
    return render(request, 'landing_page/index.html')

def signup(request):
    form = admin.UserCreationForm()
    return render(request, 'landing_page/signup.html', {'form':form})
