from django.shortcuts import render
from drillbox.forms import ToolForm


def index(request):
    form = ToolForm()
    return render(request, 'drillbox/home.html', {'form': form})


def contact(request):
    return render(request, 'drillbox/contact.html')

