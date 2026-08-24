from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1_app2(request):
    return HttpResponse ("<h1 style= 'color:green;'>vista 1 app2</h1>")
def v2_app2(request):
    return HttpResponse ("<h1 style= 'color:red;'>vista 2 app2</h1>")