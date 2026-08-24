from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1_app1(request):
    return HttpResponse ("<h1>vista 1 app1</h1>")

def v2_app2(request):
    return HttpResponse ("<h1>vista 2 app1</h1>"
    "<p>todo lo que necesitas</p>")
                        
