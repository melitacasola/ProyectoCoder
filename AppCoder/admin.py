from django.contrib import admin
from .models import * #importamos todo
 
# Register your models here.

# class AppcoderConfig(AppConfig):
    #     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'AppCoder'

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entrega)
