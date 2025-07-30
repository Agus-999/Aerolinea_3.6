from django.shortcuts import render, get_object_or_404, redirect
from .models import Avion
from .forms import AvionForm

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
