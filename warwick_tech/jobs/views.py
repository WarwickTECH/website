from django.shortcuts import render
from django.http import HttpResponseForbidden as http403
from django.core import serializers
from .models import Job, JobForm

# Create your views here.
def job_listings(request):

    # create a dictionary of all jobs in the database
    # TODO return only most recent or popular n jobs
    # TODO use ajax call to get more at bottom of page
    jobs_query = Job.objects.all()
    jobs_data = {}
    for job in jobs_query:
        jobs_data[job.title] = job

    if request.user.is_authenticated:
        return render(request, "jobs/listings.html", {"list":jobs_data})
    else:
        return http403()

def add_job(request):
    jobs_form = JobForm()
    return render(request, "jobs/add_job.html", {"form" : jobs_form})

def confirmation(request):
    # Handle the creation of the new job object
    new_job_form = JobForm(request.POST)
    new_job_form.save()
    return render(request, "jobs/confirmation.html")
