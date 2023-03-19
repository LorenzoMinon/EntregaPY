from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request,'Entrega/inicio.html')

def cursos(request):
    return render(request,'Entrega/cursos.html')

def profesores(request):
    return render(request,'Entrega/profesores.html')

def estudiantes(request):
    return render(request,'Entrega/estudiantes.html')

def entregables(request):
    return render(request,'Entrega\estudiantes.html')

def cursoFormulario(request):
    return render(request,
    "AppCoder/cursoFormulario.html")
