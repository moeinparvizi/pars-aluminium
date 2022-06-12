from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from django.template.loader import render_to_string


def index(request):
    return render(request,'base.html')

