from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import timedelta
from .models import Avion, Vuelo
from .forms import AvionForm, VueloForm

### ---- AVIONES ---- ###

def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'empleados/aviones/lista.html', {'aviones': aviones})

def detalle_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    return render(request, 'empleados/aviones/detalle_avion.html', {'avion': avion})

def nuevo_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_aviones')
    else:
        form = AvionForm()
    return render(request, 'empleados/aviones/formulario.html', {'form': form, 'avion': None})

def editar_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_aviones')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'empleados/aviones/formulario.html', {'form': form, 'avion': avion})

def eliminar_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        avion.delete()
        return redirect('gestion:lista_aviones')
    return render(request, 'empleados/aviones/eliminar.html', {'avion': avion})


### ---- VUELOS ---- ###

# Lista
def lista_vuelos(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'empleados/vuelos/lista.html', {'vuelos': vuelos})


# Crear
def crear_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            vuelo = form.save(commit=False)

            # Capturar duración calculada desde campo oculto (en segundos)
            duracion_str = request.POST.get('duracion')
            if duracion_str:
                vuelo.duracion = timedelta(seconds=int(float(duracion_str)))

            vuelo.save()
            messages.success(request, "Vuelo creado exitosamente.")
            return redirect('gestion:lista_vuelos')
    else:
        form = VueloForm()
    return render(request, 'empleados/vuelos/formulario.html', {'form': form, 'titulo': 'Crear Vuelo'})


# Editar
def editar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            vuelo = form.save(commit=False)

            # Capturar duración nuevamente en caso de cambio
            duracion_str = request.POST.get('duracion')
            if duracion_str:
                vuelo.duracion = timedelta(seconds=int(float(duracion_str)))

            vuelo.save()
            messages.success(request, "Vuelo actualizado exitosamente.")
            return redirect('gestion:lista_vuelos')
    else:
        form = VueloForm(instance=vuelo)
    return render(request, 'empleados/vuelos/formulario.html', {'form': form, 'titulo': 'Editar Vuelo'})


# Eliminar
def eliminar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    if request.method == 'POST':
        vuelo.delete()
        messages.success(request, "Vuelo eliminado exitosamente.")
        return redirect('gestion:lista_vuelos')
    return render(request, 'empleados/vuelos/eliminar.html', {'vuelo': vuelo})



# CLIENTES

from django.shortcuts import render, get_object_or_404
from .models import Vuelo

# Clientes: lista de vuelos disponibles
def vuelos_clientes_lista(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'clientes/vuelos/lista.html', {'vuelos': vuelos})

# Clientes: detalle de vuelo
def vuelos_clientes_detalle(request, pk):
    vuelo = get_object_or_404(Vuelo, pk=pk)
    return render(request, 'clientes/vuelos/detalle.html', {'vuelo': vuelo})
