from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Tarea
from .form import AgregarTarea
from django.contrib.auth.models import User
# Create your views here.


@login_required
def tareas(request):
    tareas = Tarea.objects.filter(usuario = request.user)
    usuario = request.user
    contexto = {
        'tarea':tareas,
        'user':usuario,
    }
    return render(request,'tareas.html',contexto)



def cerrar(request):
    logout(request)
    return redirect('login')

@login_required
def agregarTarea(request):
    usuario = request.user
    if request.method == 'POST':
        form = AgregarTarea(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = usuario
            tarea.save()
            aux = False
            return redirect ('tareas')
    else:
        form = AgregarTarea()
        contexto = {
            'form': form,
            'user':usuario,
            'aux':True,
        }
        return render(request,'tareas.html',contexto)


def infoTarea(request,tarea_id):
    tarea = Tarea.objects.get(id = tarea_id)
    usuario = request.user
    contexto = {
        'tarea':tarea,
        'user':usuario,
    }
    return render(request,'tarea.html',contexto)

def eliminarTarea(request,tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('tareas')

