from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html="""
    <h1 style="color=red">Estás en la vista 1</h1>
"""

    return HttpResponse(html)