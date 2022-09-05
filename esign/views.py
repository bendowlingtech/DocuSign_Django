from django.shortcuts import render
from . import embedded_signing
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'esign/index.html')

def embedded(request):
    url = embedded_signing.embedded_signing()
    response = redirect(url)
    return response







