from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from django.template.loader import render_to_string


def index(request):
    return render(request,'base.html')

def handler404(request, *args, **argv):
    return render(request,'404.html', {})
