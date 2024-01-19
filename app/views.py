from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def karim(request):
    return HttpResponse('<h1>My Name is Phatan Karim</h1>')

def phatan(request):
    return HttpResponse('<marquee><h1 style="color:red">This is Phatan Here...</h1></marquee>')