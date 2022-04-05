from django.shortcuts import render
from django.http import HttpResponse
#from models import Curso
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre= "Web", camada= "37250")
    
    curso.save()
    
    documento = f"El Curso es de: {curso.nombre}, la camada es: {curso.camada}"
    
    return HttpResponse(documento)
