from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def func_one(request):
    return HttpResponse("Hello world")
    
def func_two(request):
    return HttpResponse("Hello there")