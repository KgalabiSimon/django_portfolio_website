from django.shortcuts import render
from jobs.models import Job

# Create your views here.
def home(request):
    """View for home page"""
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return  render(request, 'jobs/home.html',context)
