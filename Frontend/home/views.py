from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def bienvenido(request):
    return HttpResponse('holi')

def bienvenidoTemplate(requests):
    return render(requests, 'home/bienvenido.html',{'nombre':'pan'})