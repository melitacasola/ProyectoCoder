from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
#from models import Curso
from .models import *
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario


# Create your views here.
# def curso(self):
#     curso = Curso(nombre= "Web", camada= "37250")
    
#     curso.save()
    
#     documento = f"El Curso es de: {curso.nombre}, la camada es: {curso.camada}"
    
#     return HttpResponse(documento)

# def inicio(request):
#     return  HttpResponse('vista inicio')

# def curso(request):
#     return HttpResponse('vista curso')

# def profesores(request):
#     return HttpResponse('vista profesores')

# def estudiantes(request):
#     return HttpResponse('vista estudiantes')

# def entregables(request):
#     return HttpResponse('vista entregables')

    
def inicio(request):
    return  render(request, "AppCoder/inicio.html")

def cursos(request):
    return  render(request, "AppCoder/cursos.html")

def profesores(request):
    return  render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return  render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return  render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
    
    if request.method == 'POST':
        
        #creamos variable
        miFormulario = CursoFormulario(request.POST) #me llega del HTML
        
        print(miFormulario)
        
        if miFormulario.is_valid:   #palabra reservada de validac de Django
            
            informacion= miFormulario.cleaned_data
            
            print(informacion)
            
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            
            curso.save()
            
            return render(request, "AppCoder/inicio.html")  #aca elijo que vuelva a inicio, sino a otro lado
        
    else:
        miFormulario= CursoFormulario() #sino vuelve al formulario vacio
        
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
            
            
def profesorFormulario(request):
    
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], Profesion=informacion['Profesion'])
            
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario= ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):
    
    if request.GET["camada"]:
        
        #respuesta = f"estoy buscando la camada nro: {request.GET['camada']}"
        camada = request.GET['camada']
        print(camada)
        cursos = Curso.objects.filter(camada__icontains=camada)
        print(cursos)
        
        return render(request, "AppCoder/resultadosBusqueda.html", {"curso": cursos, "camada": camada})
    
    else:
        respuesta = "No olvidarse Datos"
    #return HttpResponse(respuesta)
    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})