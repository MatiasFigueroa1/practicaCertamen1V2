from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista2(request):
    html="""
    <h1 style="color:red">Estás en la vista2</h1>
    <a class="btn btn-outline-primary" href="/" > Ir a vista1</a>
"""
    return  HttpResponse(html)