from django.shortcuts import render
from drillbox.models import Tool

def index(request):
    tools = Tool.objects.all()

    context = {
        'tools':tools
    }

    return render(request, 'drillbox/home.html', context)


def contact(request):
    return render(request, 'drillbox/contact.html')

