from django.shortcuts import render

# Create your views here.
from .models import Jobs

def index(request):
	jobs = Jobs.objects
	return render(request,'jobs/index.html',context={
		'jobs':jobs
		})