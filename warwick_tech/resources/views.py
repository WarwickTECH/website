from django.shortcuts import render
from django.http import HttpResponseForbidden as http403

# Create your views here.
def resources(request):
    data_dict = {"page_title":"Resources", "app_name":"resources"}
    if request.user.is_authenticated:
        return render(request, "resources/resource_page.html", data_dict)
    else:
        return http403()
