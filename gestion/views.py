from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import timedelta
from .models import Avion, Vuelo, Asiento
from .forms import AvionForm, VueloForm

### ---- AVIONES ---- ###

def lista_aviones(request):
    aviones = Avion.objects.all()
    return render(request, 'empleados/aviones/lista.html', {'aviones': aviones})

def detalle_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    return render(request, 'empleados/aviones/detalle_avion.html', {'avion': avion})

def columna_a_letras(n):
    letras = ''
    while n > 0:
        n, resto = divmod(n - 1, 26)
        letras = chr(65 + resto) + letras
    return letras

def nuevo_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST, request.FILES)
        if form.is_valid():
            avion = form.save()

            filas = avion.filas
            columnas = avion.columnas
            capacidad = avion.capacidad

            if filas * columnas < capacidad:
                messages.error(request, "La capacidad del avión no es suficiente para las filas y columnas configuradas.")
                return redirect('gestion:nuevo_avion')

            # Asignar tipos de asiento
            for fila in range(1, filas + 1):
                for col in range(1, columnas + 1):
                    letra_columna = columna_a_letras(col)
                    numero = f"{fila}{letra_columna}"

                    # Asignar tipo de asiento según la fila
                    if fila <= 2:
                        tipo = 'primera'
                    elif fila <= 6:
                        tipo = 'ejecutivo'
                    elif fila <= 10:
                        tipo = 'premium'
                    else:
                        tipo = 'economico'

                    # Crear el asiento con tipo y estado
                    Asiento.objects.create(
                        avion=avion,
                        numero=numero,
                        fila=fila,
                        columna=col,
                        tipo=tipo,  # Solo tipo, sin precio
                        estado='disponible'  # Estado inicial
                    )

            messages.success(request, "Avión y asientos creados correctamente.")
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


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pasajero
from .forms import PasajeroForm

# Lista de pasajeros
def lista_pasajeros(request):
    pasajeros = Pasajero.objects.all()
    return render(request, 'empleados/pasajeros/lista.html', {'pasajeros': pasajeros})

# Crear pasajero
def nuevo_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pasajero creado correctamente.")
            return redirect('gestion:lista_pasajeros')
        else:
            messages.error(request, "Formulario inválido. Por favor revisa los datos.")
    else:
        form = PasajeroForm()
    return render(request, 'empleados/pasajeros/formulario.html', {'form': form, 'pasajero': None})

# Editar pasajero
def editar_pasajero(request, pasajero_id):
    pasajero = get_object_or_404(Pasajero, id=pasajero_id)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
            messages.success(request, "Pasajero actualizado correctamente.")
            return redirect('gestion:lista_pasajeros')
        else:
            messages.error(request, "Formulario inválido. Por favor revisa los datos.")
    else:
        form = PasajeroForm(instance=pasajero)
    return render(request, 'empleados/pasajeros/formulario.html', {'form': form, 'pasajero': pasajero})

# Eliminar pasajero
def eliminar_pasajero(request, pasajero_id):
    pasajero = get_object_or_404(Pasajero, id=pasajero_id)
    if request.method == 'POST':
        pasajero.delete()
        messages.success(request, "Pasajero eliminado correctamente.")
        return redirect('gestion:lista_pasajeros')
    return render(request, 'empleados/pasajeros/eliminar.html', {'pasajero': pasajero})


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


from decimal import Decimal
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from .models import Reserva, Vuelo, Pasajero, Asiento
from .forms import ReservaForm

# Precios de asientos (disponible globalmente)
PRECIOS_ASIENTO = {
    'economico': Decimal('100.00'),
    'premium': Decimal('200.00'),
    'ejecutivo': Decimal('300.00'),
    'primera': Decimal('400.00'),
}


@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).prefetch_related('asientos').order_by('-fecha_reserva')
    return render(request, "clientes/reservas/lista.html", {"reservas": reservas})


@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            documento = form.cleaned_data['documento']
            nombre = form.cleaned_data['nombre']
            vuelo = form.cleaned_data['vuelo']

            if not (documento and nombre and vuelo):
                messages.error(request, "Por favor, completa todos los campos obligatorios.")
                return render(request, 'clientes/reservas/formulario.html', {'form': form, 'reserva': None})

            pasajero, _ = Pasajero.objects.get_or_create(
                documento=documento,
                defaults={
                    'nombre': nombre,
                    'email': form.cleaned_data.get('email', ''),
                    'telefono': form.cleaned_data.get('telefono', ''),
                    'fecha_nacimiento': form.cleaned_data.get('fecha_nacimiento'),
                    'tipo_documento': form.cleaned_data.get('tipo_documento', 'otro'),
                    'usuario': request.user,
                }
            )

            reserva = Reserva.objects.create(
                vuelo=vuelo,
                pasajero=pasajero,
                usuario=request.user,
                estado='pendiente',
                precio=Decimal('0.00'),
                codigo_reserva=str(get_random_string(8)).upper()
            )

            # ✅ Crear boleto automáticamente
            Boleto.objects.create(
                reserva=reserva,
                codigo_barra=f"BOL-{get_random_string(12).upper()}",
                estado='emitido'
            )

            return redirect('gestion:ver_asientos', reserva_id=reserva.id)
        else:
            messages.error(request, "Formulario inválido. Por favor revisa los datos.")
    else:
        form = ReservaForm()

    return render(request, 'clientes/reservas/formulario.html', {'form': form, 'reserva': None})

@login_required
def ver_asientos(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    vuelo = reserva.vuelo
    asientos = Asiento.objects.filter(avion=vuelo.avion)

    asientos_reserva = reserva.asientos.all()

    for asiento in asientos:
        asiento.precio = PRECIOS_ASIENTO.get(asiento.tipo, Decimal('0.00'))
        asiento.ocupado = asiento.estado == 'ocupado' and asiento not in asientos_reserva
        asiento.es_mio = asiento in asientos_reserva

    return render(request, 'clientes/reservas/reserva.html', {
        'reserva': reserva,
        'vuelo': vuelo,
        'asientos': asientos,
    })


@login_required
@csrf_exempt
def confirmar_compra(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            asiento_ids = data.get("asiento_ids", [])
            reserva_id = data.get("reserva_id")

            if not asiento_ids:
                return JsonResponse({"success": False, "error": "No se enviaron asientos."})

            reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
            total_precio = Decimal("0.00")

            with transaction.atomic():
                # Liberar los asientos actuales
                for asiento in reserva.asientos.select_for_update():
                    asiento.estado = "disponible"
                    asiento.save()

                reserva.asientos.clear()

                # Asignar nuevos asientos
                for asiento_id in asiento_ids:
                    asiento = Asiento.objects.select_for_update().get(id=asiento_id)
                    if asiento.estado == "ocupado":
                        return JsonResponse({"success": False, "error": f"Asiento {asiento.numero} ya está ocupado."})

                    asiento.estado = "ocupado"
                    asiento.save()

                    total_precio += PRECIOS_ASIENTO.get(asiento.tipo, Decimal("0.00"))
                    reserva.asientos.add(asiento)

                reserva.estado = "confirmada"
                reserva.precio = total_precio
                reserva.save()

            return JsonResponse({
                "success": True,
                "total": str(total_precio),
                "reserva_id": reserva.id,
            })

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Método no permitido."})


@login_required
def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    pasajero = reserva.pasajero

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    vuelo_nuevo = form.cleaned_data['vuelo']
                    if vuelo_nuevo != reserva.vuelo:
                        for asiento in reserva.asientos.all():
                            asiento.estado = 'disponible'
                            asiento.save()
                        reserva.asientos.clear()
                        reserva.vuelo = vuelo_nuevo

                    pasajero.nombre = form.cleaned_data['nombre']
                    pasajero.documento = form.cleaned_data['documento']
                    pasajero.email = form.cleaned_data.get('email', '')
                    pasajero.telefono = form.cleaned_data.get('telefono', '')
                    pasajero.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
                    pasajero.tipo_documento = form.cleaned_data.get('tipo_documento', 'otro')
                    pasajero.save()

                    reserva.estado = 'pendiente'
                    reserva.precio = Decimal('0.00')
                    reserva.save()

                    messages.success(request, 'Reserva actualizada correctamente. Por favor, selecciona los asientos nuevamente.')
                    return redirect('gestion:ver_asientos', reserva_id=reserva.id)

            except Exception as e:
                messages.error(request, f'Error al actualizar reserva: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        initial = {
            'vuelo': reserva.vuelo,
            'nombre': pasajero.nombre,
            'documento': pasajero.documento,
            'email': pasajero.email,
            'telefono': pasajero.telefono,
            'fecha_nacimiento': pasajero.fecha_nacimiento,
            'tipo_documento': pasajero.tipo_documento,
        }
        form = ReservaForm(initial=initial)

    return render(request, 'clientes/reservas/detalle.html', {
        'reserva': reserva,
        'form': form,
    })

@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            documento = form.cleaned_data['documento']
            nombre = form.cleaned_data['nombre']
            vuelo = form.cleaned_data['vuelo']

            if not (documento and nombre and vuelo):
                messages.error(request, "Por favor, completa todos los campos obligatorios.")
                return render(request, 'clientes/reservas/formulario.html', {'form': form, 'reserva': reserva})

            pasajero = reserva.pasajero
            pasajero.nombre = nombre
            pasajero.documento = documento
            pasajero.email = form.cleaned_data.get('email', '')
            pasajero.telefono = form.cleaned_data.get('telefono', '')
            pasajero.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            pasajero.tipo_documento = form.cleaned_data.get('tipo_documento', 'otro')
            pasajero.save()

            if vuelo != reserva.vuelo:
                for asiento in reserva.asientos.all():
                    asiento.estado = 'disponible'
                    asiento.save()
                reserva.asientos.clear()

            reserva.vuelo = vuelo
            reserva.save()

            messages.success(request, "Reserva actualizada correctamente.")
            return redirect('gestion:detalle_reserva', reserva_id=reserva.id)
        else:
            messages.error(request, "Formulario inválido. Por favor revisa los datos.")
    else:
        initial_data = {
            'vuelo': reserva.vuelo,
            'nombre': reserva.pasajero.nombre,
            'documento': reserva.pasajero.documento,
            'email': reserva.pasajero.email,
            'telefono': reserva.pasajero.telefono,
            'fecha_nacimiento': reserva.pasajero.fecha_nacimiento,
            'tipo_documento': reserva.pasajero.tipo_documento,
        }
        form = ReservaForm(initial=initial_data)

    return render(request, 'clientes/reservas/formulario.html', {'form': form, 'reserva': reserva})

@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    if request.method == 'POST':
        with transaction.atomic():
            for asiento in reserva.asientos.select_for_update():
                asiento.estado = 'disponible'
                asiento.save()

            reserva.asientos.clear()
            reserva.delete()

        messages.success(request, 'Reserva cancelada y asientos liberados.')
        return redirect('gestion:mis_reservas')

    return render(request, 'clientes/reservas/eliminar.html', {'reserva': reserva})


from .models import Reserva, Vuelo, Pasajero, Asiento, Boleto  # ← agregamos Boleto

@login_required
def ver_boleto(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    # Asegurar que exista un boleto (por si la reserva es vieja)
    boleto = getattr(reserva, 'boleto', None)
    if boleto is None:
        boleto = Boleto.objects.create(
            reserva=reserva,
            codigo_barra=f"BOL-{get_random_string(12).upper()}",
            estado='emitido'
        )

    asientos = list(reserva.asientos.all())
    return render(request, 'clientes/boletos/boleto.html', {
        'reserva': reserva,
        'boleto': boleto,
        'asientos': asientos,
    })
@login_required
def descargar_boleto(request, reserva_id):
    """
    Vista que muestra/permite descargar el boleto en formato HTML imprimible (guarda como PDF desde el navegador).
    Crea el Boleto si por alguna razón no existe (reservas antiguas).
    """
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    # Asegurar existencia del boleto (si por alguna razón no fue creado antes)
    boleto = getattr(reserva, 'boleto', None)
    if boleto is None:
        boleto = Boleto.objects.create(
            reserva=reserva,
            codigo_barra=f"BOL-{get_random_string(12).upper()}",
            estado='emitido'
        )

    asientos = list(reserva.asientos.all())
    return render(request, 'clientes/boletos/boleto.html', {
        'reserva': reserva,
        'boleto': boleto,
        'asientos': asientos,
    })