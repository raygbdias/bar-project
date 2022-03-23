from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Pick your poison")

# Create your views here.
