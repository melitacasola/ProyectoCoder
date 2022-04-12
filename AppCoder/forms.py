import email
from django import forms

class CursoFormulario(forms.Form):
    
    #especificar los campos
    curso= forms.CharField(max_length=40)
    camada= forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    Profesion= forms.CharField(max_length=30)
    
    