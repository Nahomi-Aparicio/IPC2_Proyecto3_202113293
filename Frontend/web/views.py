from contextlib import redirect_stderr
from importlib.resources import contents
from django.shortcuts import render, redirect
import requests
import json

# Create your views here.

endpoint="http://localhost:5000{}"

#--------------------------cargar datos -------------------------------------------
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

#--------------------------consultar datos -------------------------------------------
def consultar(request):
    if request.method =='GET':
        url=endpoint.format('/consultandoDatos')
        data=requests.get(url)
        context={
            'data':data.json(),
           
        }
       
        return render(request, 'mostrardatos.html', context)
 
#--------------------------agregar recursos  1 x-------------------------------------------

def agregarRE(request):
    if request.method =='GET':
        url=endpoint.format('/crearRecurso')
        data=requests.get(url)
        contex2={
            'data':data.text,
        }
        return render(request, 'recursos.html', contex2)
        
    elif request.method =='POST':
        id=request.POST.get('id')
        nombre=request.POST.get('nombre')
        abreviatura=request.POST.get('abreviatura')
        metrica=request.POST.get('metrica')
        tipo=request.POST.get('tipo')
        valorXhora=request.POST.get('valorXhora')
        url=endpoint.format('/crearRecurso')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista=str(id)
        lista+=','
        lista+=str(nombre)
        lista+=','
        lista+=str(abreviatura)
        lista+=','
        lista+=str(metrica)
        lista+=','
        lista+=str(tipo)
        lista+=','
        lista+=str(valorXhora)
        requests.post(url,str(lista) )
        lista=''
        return redirect('agregarRE')

#--------------------------agregar categoria 2 x-------------------------------------------

def categori(request):
    if request.method =='GET':
        url=endpoint.format('/crearCategoria')
        data=requests.get(url)
        contexr={
            'data':data.text,
        }
        return render(request, 'categorias.html', contexr)
        
    elif request.method =='POST':
        id=request.POST.get('id')
      
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        cargaTrabajo=request.POST.get('cargaTrabajo')
       
        url=endpoint.format('/crearCategoria')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista1=str(id)
        lista1+=','
       
        lista1+=str(nombre)
        lista1+=','
        lista1+=str(descripcion)
        lista1+=','
        lista1+=str(cargaTrabajo)
        
        requests.post(url,str(lista1) )
        lista1=''
        return redirect('categori')

def confica(request):

    if request.method =='GET':
        url=endpoint.format('/crearConfiguracion')
        data=requests.get(url)
        contexh={
            'data':data.text,
        }
        return render(request, 'configuracion.html', contexh)
        
    elif request.method =='POST':
        id=request.POST.get('id')
        id2=request.POST.get('id2')
        nombre=request.POST.get('nombre')
        descripcion=request.POST.get('descripcion')
        idRc=request.POST.get('idRc')
        cantidad=request.POST.get('Recursos')
        url=endpoint.format('/crearConfiguracion')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista2=str(id)
        lista2+=','
        lista2+=str(id2)
        lista2+=','

        lista2+=str(nombre)
        lista2+=','
        lista2+=str(descripcion)
        lista2+=','
        lista2+=str(idRc)
        lista2+=','
        lista2+=str(cantidad)
       
        requests.post(url,str(lista2) )
        lista2=''
        return redirect('confica')

#--------------------------agregar cliente 4   x-------------------------------------------
def cliente(request):
    if request.method =='GET':
        url=endpoint.format('/crearCliente')
        data=requests.get(url)
        contexh={
            'data':data.text,
        }
        return render(request, 'crearCliente.html', contexh)
        
    elif request.method =='POST':
        nit=request.POST.get('nit')
        nombre=request.POST.get('nombre')
        usuario=request.POST.get('usuario')
        direccion=request.POST.get('direccion')
        correoElectronico=request.POST.get('correoElectronico')
       
        url=endpoint.format('/crearCliente')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista3=str(nit)
        lista3+=','
        lista3+=str(nombre)
        lista3+=','

        lista3+=str(usuario)
        lista3+=','
        lista3+=str(direccion)
        lista3+=','
        lista3+=str(correoElectronico)
       
        requests.post(url,str(lista3) )
        lista3=''
        
        return redirect('cliente')

#--------------------------agregar proyecto instancia   x-------------------------------------------
def instancia(request):
    if request.method =='GET':
        url=endpoint.format('/crearInstancia')
        data=requests.get(url)
        contexh={
            'data':data.text,
        }
        return render(request, 'crearInstancia.html', contexh)
        
    elif request.method =='POST':
        id=request.POST.get('id')
        idConfiguracion=request.POST.get('idConfiguracion')
        nombre=request.POST.get('nombre')
        fechaInicio=request.POST.get('fechaInicio')
        estado=request.POST.get('estado')
        fechaFinal=request.POST.get('fechaFinal')
       
        url=endpoint.format('/crearInstancia')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista4=str(id)
        lista4+=','
        lista4+=str(idConfiguracion)
        lista4+=','
        lista4+=str(nombre)
        lista4+=','
        lista4+=str(fechaInicio)
        lista4+=','

        lista4+=str(estado)
        lista4+=','
        lista4+=str(fechaFinal)
       
        print(lista4)
        requests.post(url,str(lista4) )
        lista4=''
        
        return redirect('instancia')

#--------------------------crear factura x-------------------------------------------

def facturita(request):
    if request.method =='GET':
        url=endpoint.format('/crearFactura')
        data=requests.get(url)
        contexjh={
            'data':data.text,
        }
        return render(request, 'crearFactura.html', contexjh)
        
    elif request.method =='POST':
        nit=request.POST.get('nit')
        inicial=request.POST.get('inicial')
        final=request.POST.get('final')
       
        url=endpoint.format('/crearFactura')
        #print({'id':id,'nombre':nombre,'abreviatura':abreviatura,'metrica':metrica,'tipo':tipo,'valorXhora':valorXhora})
        lista6=str(nit)
        lista6+=','
        lista6+=str(inicial)
        lista6+=','
        lista6+=str(final)
        print(lista6)
       
        requests.post(url,str(lista6) )
        lista6=''
       
        return redirect('facturita')