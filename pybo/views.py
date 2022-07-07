from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕 난 pybo임.")

# Create your views here.
