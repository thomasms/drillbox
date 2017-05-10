from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'drillbox/home.html')

def contact(request):
    return render(request, 'drillbox/basic.html', {'content':['For all issues relating to DrillBox, please contact us at','contact@bareit.uk']})
