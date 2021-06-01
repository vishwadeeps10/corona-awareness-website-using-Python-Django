from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'webapp/homepage.html')

def webpage1(request):
    return render(request,'webapp/page1.html')

def webpage2(request):
    return render(request,'webapp/page2.html')

def webpage3(request):
    return render(request,'webapp/page3.html')

def webpage4(request):
    return render(request,'webapp/page4.html')
