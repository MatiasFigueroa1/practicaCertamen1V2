from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html="""
    <h1 style="color:blue">Estás en la vista 1</h1>
    <a href="/vista2/" > Ir a vista 2 </a>
"""

    return HttpResponse(html)