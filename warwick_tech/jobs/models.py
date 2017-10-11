from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Job(models.Model):
    """ Class describing the job object for the mysql database """

    title = models.CharField(max_length=256)
    company_name = models.CharField(max_length=100, default="")
    contact_info = models.EmailField()
    description = models.TextField()
    requirements = models.TextField(blank=True)
    issue_date = models.DateTimeField("date issued", default=timezone.now)
    due_date = models.DateTimeField("Deadline", blank=True)
    info_link = models.URLField(blank=True)

    # Optional phone number
    message = "Phone number must be entered in the format: '+999999999'. " + \
    "Up to 15 digits allowed."
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=message)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
