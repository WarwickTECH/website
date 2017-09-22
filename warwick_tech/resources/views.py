from django.shortcuts import render
from django.http import HttpResponseForbidden as http403

# Create your views here.
def resources(request):
    if request.user.is_authenticated:
        return render(request, "resources/resource_page.html")
    else:
        return http403()
