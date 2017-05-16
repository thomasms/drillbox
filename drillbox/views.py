from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'drillbox/home.html')

def contact(request):
    return render(request, 'drillbox/contact.html')
