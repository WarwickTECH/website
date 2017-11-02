from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.job_listings, name="jobs_listings"),
    url(r'^add_job$', views.add_job, name="add_job")
]
