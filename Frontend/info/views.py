from django.shortcuts import render
from .servicios import servicios

# Create your views here.
def consultaDatos(request):
    consultaDatos=servicios.getServicios()
    result=""
    if request.method=="POST":
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        result=servicios.creandoServicio({'nombre':nombre,'apellido':apellido})



    return render(request, 'info/info.html', {'listaDatos':consultaDatos,'result':result})