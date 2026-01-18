from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html')

def resume(request):
    return render(request, 'main/resume.html')

def health(request):
    return HttpResponse("OK", content_type="text/plain")
