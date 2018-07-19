from django import forms

from .models import Tarea

class AgregarTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'fechaInicio',
            'fechaTermino',
            'usuario',
            'estado',
            'tipo',
        ]

        labels = {
            'titulo':'Título de la nueva tarea',
            'descripcion':'Descripción',
            'fechaInicio':'Fecha de inicio',
            'fechaTermino':'Fecha de término',
            'usuario':'User',
            'estado':'Estado de la tarea',
            'tipo':'tipo de la tarea',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'class':'form-control'}),
            'fechaTermino': forms.DateInput(attrs={'class':'form-control'}),
            'usuario': forms.HiddenInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
        }


