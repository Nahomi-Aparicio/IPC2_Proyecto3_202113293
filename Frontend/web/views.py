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

def agregarRE(request):
    if request.method =='GET':
        url=endpoint.format('/crearRecurso')
        data=requests.get(url)
        context={
            'data':data.json,
        }
        return render(request, 'recursos.html', context)
    elif request.method =='POST':
        id=request.POST.get('id')
        nombre=request.POST.get('nombre')
        abreviatura=request.POST.get('abreviatura')
        metrica=request.POST.get('metrica')
        tipo=request.POST.get('tipo')
        valorXhora=request.POST.get('valorXhora')
        url=endpoint.format('/crearRecurso')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        requests.post(url,{'id':id,'nombre': nombre,'abreviatura': abreviatura,'metrica': metrica,'tipo':tipo,'valorXhora': valorXhora})
        return redirect('agregarRE')
   