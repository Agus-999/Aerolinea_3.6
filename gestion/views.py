from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import timedelta
from .models import Avion, Vuelo
from .forms import AvionForm, VueloForm

### ---- AVIONES ---- ###

# Lista
def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'empleados/aviones/lista.html', {'aviones': aviones})

# Crear / Editar
def avion_formulario(request, pk=None):
    avion = get_object_or_404(Avion, pk=pk) if pk else None

    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_aviones')
    else:
        form = AvionForm(instance=avion)

    return render(request, 'empleados/aviones/formulario.html', {'form': form, 'avion': avion})

# Eliminar
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
