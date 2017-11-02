from django.shortcuts import render
from django.http import HttpResponseForbidden as http403
from django.core import serializers
from .models import Job

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
    #TODO get job form

    return render(request, "jobs/add_job.html")
