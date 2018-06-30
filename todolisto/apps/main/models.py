from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Estado(models.Model):
    nombreEstado = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombreEstado)

class Tipotarea(models.Model):
    nombreTarea = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombreTarea)


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    fechaInicio = models.DateTimeField(default=datetime.date.today)
    fechaTermino = models.DateTimeField(default=datetime.date.today)
    usuario = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,blank=True,null=True,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipotarea,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.titulo)