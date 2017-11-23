from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden as http403
from django.core import serializers
from .models import Job, JobForm
from landing_page.admin import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def job_listings(request):

    # create a dictionary of all jobs in the database
    # TODO return only most recent or popular n jobs
    # TODO use ajax call to get more at bottom of page

    # Handle new users
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.clean_password2()
            user = authenticate(email=email, password=password)
            login(request, user)
        else:
            return redirect('signup')

    jobs_query = Job.objects.all()

    if request.user.is_authenticated:
        return render(request, "jobs/listings.html", {"list":jobs_query})
    else:
        return http403()

def add_job(request):
    jobs_form = JobForm()
    data_dict = {"form": jobs_form, "page_title": "Add Job", "app_name": "job"}
    return render(request, "jobs/add_job.html", data_dict)

def confirmation(request):
    # Handle the creation of the new job object
    new_job_form = JobForm(request.POST)
    new_job_form.save()
    data_dict = {"page_title": "Success", "app_name": "job"}
    return render(request, "jobs/confirmation.html", data_dict)
