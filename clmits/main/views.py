from django.shortcuts import render
from .models import Experience
# Create your views here.
def homepage(res):
    return render (request=res, template_name= 'main/index.html', context={'experiences':Experience.objects.all()})