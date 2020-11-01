from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
  return render(request,'index.html')

def showAbout(request):
  return render(request, 'about.html')
# Create your views here.

def showProjects(request):
  return render(request, 'projects.html')

def showContact(request):
  return render(request, 'contact.html')