
from django.shortcuts import render

# original_akindo/views.py
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
