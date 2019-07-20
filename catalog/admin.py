from django.contrib import admin

# Register your models here.
from .models import Carrera, Alumno 

admin.site.register(Carrera)
admin.site.register(Alumno)
