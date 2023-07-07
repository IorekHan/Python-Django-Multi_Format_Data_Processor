from django.shortcuts import render
from django.http import HttpResponse


def base_view(request):
    return render(request, 'base.html')


def index_view(request):
    return render(request, 'index.html')