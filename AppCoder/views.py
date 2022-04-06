from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
#from models import Curso
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre= "Web", camada= "37250")
    
    curso.save()
    
    documento = f"El Curso es de: {curso.nombre}, la camada es: {curso.camada}"
    
    return HttpResponse(documento)

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