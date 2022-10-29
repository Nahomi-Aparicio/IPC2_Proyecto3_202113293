from contextlib import redirect_stderr
from importlib.resources import contents
from django.shortcuts import render, redirect
import requests
# Create your views here.

endpoint="http://localhost:5000{}"


def cargar(request):
    if request.method =='GET':
        url=endpoint.format('/cargarDatos')
        data=requests.get(url)
        context={
            'data':data.text,
            
        }
                 
        return render(request, 'cargar.html', context)
    elif request.method =='POST':      
        docs=request.POST.get('docs')        
        url=endpoint.format('/cargarDatos')
        requests.post(url, docs)
        
        return redirect('cargar')

def consultar(request):
    if request.method =='GET':
        url=endpoint.format('/consultandoDatos')
        data=requests.get(url)
        context={
            'data':data.json,
        }       
        return render(request, 'mostrardatos.html', context)
   
def  consumar(request):
    if request.method =='GET':
        url=endpoint.format('/cargarDatos2')
        data=requests.get(url)
        context={
            'data':data.text,
        }
        return render(request, 'consumos.html', context)
    elif request.method =='POST':
        docs=request.POST.get('docs')
        url=endpoint.format('/cargarDatos2')
        requests.post(url, docs)
        return redirect('consumos')

        

   