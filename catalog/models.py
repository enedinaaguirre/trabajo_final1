from django.db import models
from django.urls import reverse

# Create your models here.


class Carrera(models.Model):
     """Modelo para representar Carrera."""
     nombre = models.CharField(max_length=100) 
     #apellidos = models.CharField(max_length=100)
     imagen = models.CharField(max_length=100)
    
     
     def get_absolute_url(self):
         return reverse('detalles-carrera', args=[str(self.id)])

     def __str__(self):
         """Cadena para representar los objetos de carrera."""
         #return '{0} {1}'.format(self.nombre, self.apellidos)
         return self.nombre 

class Alumno(models.Model):
     """Modelo para representar Carrera."""
     nombre = models.CharField(max_length=200)
     apellidos = models.CharField(max_length=100)
     carrera= models.ForeignKey('Carrera', on_delete=models.SET_NULL, null=True)
    
     def __str__(self):        
         """Cadena para representar los objetos de carrera."""
         #return self.nombre 
         return '{0} {1}'.format(self.nombre, self.apellidos)


