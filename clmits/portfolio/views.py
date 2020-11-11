from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def portfolio(res):
    return render (request=res, template_name= 'portfolio/index.html')