from django.shortcuts import render
import datetime

def index(request):
    return render(request, 'main/index.html')

def events(request):
    return render(request, 'main/events.html')
