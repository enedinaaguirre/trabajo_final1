from django.shortcuts import render

from .models import Carrera, Alumno

# Create your views here.
def index(request):
	m = Alumno.objects.all()
	return render(request, "alumnos/index.html", { 'alumnos': m })

def detalles(request, pk):
	carrera = Carrera.objects.get(pk=pk)
	return render(request, "carreras/show.html", { 'carrera': carrera })