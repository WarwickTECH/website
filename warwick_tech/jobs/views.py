from django.shortcuts import render
from django.http import HttpResponseForbidden as http403

# Create your views here.
def job_listings(request):
    if request.user.is_authenticated:
        return render(request, "jobs/listings.html")
    else:
        return http403()
