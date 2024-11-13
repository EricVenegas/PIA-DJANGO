from django.shortcuts import render, HttpResponse
from .models import TodoItem
from .forms import ComentarioForm  # Importamos el formulario

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def futuro(request):
    return render(request, "futuro.html")

def contacto(request):
    return render(request, "contacto.html")


def nutricional(request):
    return render(request, "nutricional.html")


def sabores(request):
    return render(request, "sabores.html")


def contacto(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el comentario en la base de datos
            
    else:
        form = ComentarioForm()  # Si es GET, mostramos el formulario vacío

    return render(request, 'contacto.html', {'form': form})