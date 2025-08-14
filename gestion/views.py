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

from decimal import Decimal
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string

from .models import Reserva, Vuelo, Pasajero, Asiento, Boleto
from .forms import ReservaEmpleadoForm, PasajeroForm

# Precios por tipo de asiento
PRECIOS_ASIENTO = {
    'economico': Decimal('100.00'),
    'premium': Decimal('200.00'),
    'ejecutivo': Decimal('300.00'),
    'primera': Decimal('400.00'),
}

@login_required
def lista_reservas_empleado(request):
    reservas = Reserva.objects.prefetch_related('asientos').order_by('-fecha_reserva')
    return render(request, 'empleados/reservas/lista_reservas.html', {'reservas': reservas})


@login_required
def crear_reserva_empleado(request):
    if request.method == 'POST':
        reserva_form = ReservaEmpleadoForm(request.POST)

        # Tomamos los datos del pasajero directamente
        nombre = request.POST.get('nombre')
        documento = request.POST.get('documento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        tipo_documento = request.POST.get('tipo_documento')

        if reserva_form.is_valid() and nombre and documento:
            with transaction.atomic():
                pasajero, _ = Pasajero.objects.get_or_create(
                    documento=documento,
                    defaults={
                        'nombre': nombre,
                        'email': email,
                        'telefono': telefono,
                        'fecha_nacimiento': fecha_nacimiento,
                        'tipo_documento': tipo_documento,
                        'usuario': request.user,  # opcional, asignamos empleado como creador
                    }
                )

                reserva = reserva_form.save(commit=False)
                reserva.pasajero = pasajero
                reserva.usuario = request.user
                reserva.precio = Decimal('0.00')  # se calculará después
                reserva.codigo_reserva = str(get_random_string(8)).upper()
                reserva.save()

                # Crear boleto automático
                Boleto.objects.create(
                    reserva=reserva,
                    codigo_barra=f"BOL-{get_random_string(12).upper()}",
                    estado='emitido'
                )

                messages.success(request, "Reserva creada. Selecciona los asientos.")
                return redirect('gestion:ver_asientos_empleado', reserva_id=reserva.id)
        else:
            messages.error(request, "Corrige los errores en el formulario de reserva.")

    else:
        reserva_form = ReservaEmpleadoForm()

    return render(request, 'empleados/reservas/formulario_reserva.html', {
        'reserva_form': reserva_form,
    })


@login_required
def ver_asientos_empleado(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    vuelo = reserva.vuelo
    asientos = Asiento.objects.filter(avion=vuelo.avion).order_by('fila', 'columna')
    asientos_reserva = reserva.asientos.all()

    for asiento in asientos:
        asiento.precio = PRECIOS_ASIENTO.get(asiento.tipo, Decimal('0.00'))
        asiento.ocupado = asiento.estado == 'ocupado' and asiento not in asientos_reserva
        asiento.es_mio = asiento in asientos_reserva
        # Asegurar que tenga nombre para mostrar
        if not hasattr(asiento, 'nombre'):
            asiento.nombre = f"Asiento {asiento.fila}{asiento.columna}"

    return render(request, 'empleados/reservas/asientos.html', {
        'reserva': reserva,
        'vuelo': vuelo,
        'asientos': asientos,
    })



@login_required
@csrf_exempt
def confirmar_compra_empleado(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            asiento_ids = data.get("asiento_ids", [])
            reserva_id = data.get("reserva_id")
            reserva = get_object_or_404(Reserva, id=reserva_id)

            total_precio = Decimal("0.00")
            with transaction.atomic():
                # Liberar asientos anteriores
                for asiento in reserva.asientos.select_for_update():
                    asiento.estado = "disponible"
                    asiento.save()
                reserva.asientos.clear()

                # Asignar nuevos asientos
                for asiento_id in asiento_ids:
                    asiento = Asiento.objects.select_for_update().get(id=asiento_id)
                    if asiento.estado == "ocupado":
                        return JsonResponse({"success": False, "error": f"Asiento {asiento.numero} ya ocupado."})
                    asiento.estado = "ocupado"
                    asiento.save()
                    reserva.asientos.add(asiento)
                    total_precio += PRECIOS_ASIENTO.get(asiento.tipo, Decimal("0.00"))

                reserva.precio = total_precio
                reserva.estado = "confirmada"
                reserva.save()

            return JsonResponse({"success": True, "total": str(total_precio), "reserva_id": reserva.id})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Método no permitido."})


@login_required
def detalle_reserva_empleado(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    pasajero = reserva.pasajero

    # Calculamos el precio de cada asiento
    asientos_con_precio = []
    total_precio = Decimal('0.00')
    for asiento in reserva.asientos.all():
        asiento.precio = PRECIOS_ASIENTO.get(asiento.tipo, Decimal('0.00'))
        asientos_con_precio.append(asiento)
        total_precio += asiento.precio

    if request.method == 'POST':
        reserva_form = ReservaEmpleadoForm(request.POST, instance=reserva)
        pasajero_form = PasajeroForm(request.POST, instance=pasajero)

        if reserva_form.is_valid() and pasajero_form.is_valid():
            with transaction.atomic():
                pasajero_form.save()
                reserva_form.save()
                # Reiniciar precio y estado de asientos si cambia el vuelo
                if 'vuelo' in reserva_form.changed_data:
                    for asiento in reserva.asientos.all():
                        asiento.estado = 'disponible'
                        asiento.save()
                    reserva.asientos.clear()
                    reserva.precio = Decimal('0.00')
                reserva.save()
                messages.success(request, "Reserva actualizada correctamente.")
                return redirect('gestion:detalle_reserva_empleado', reserva_id=reserva.id)
        else:
            messages.error(request, "Corrige los errores en los formularios.")
    else:
        reserva_form = ReservaEmpleadoForm(instance=reserva)
        pasajero_form = PasajeroForm(instance=pasajero)

    return render(request, 'empleados/reservas/detalle_reserva.html', {
        'reserva_form': reserva_form,
        'pasajero_form': pasajero_form,
        'reserva': reserva,
        'asientos': asientos_con_precio,  # Pasamos los asientos con precio
        'total_precio': total_precio,     # Pasamos el total
    })




@login_required
def eliminar_reserva_empleado(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        with transaction.atomic():
            for asiento in reserva.asientos.select_for_update():
                asiento.estado = 'disponible'
                asiento.save()
            reserva.asientos.clear()
            reserva.delete()
        messages.success(request, "Reserva eliminada correctamente.")
        return redirect('gestion:lista_reservas_empleado')

    return render(request, 'empleados/reservas/eliminar_reserva.html', {'reserva': reserva})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Boleto

@login_required
def lista_boletos_empleado(request):
    boletos = Boleto.objects.select_related('reserva', 'reserva__pasajero', 'reserva__vuelo').all()
    return render(request, 'empleados/boletos/lista_boletos.html', {
        'boletos': boletos,
    })

@login_required
def verificar_boleto_empleado(request, codigo):
    boleto = get_object_or_404(
        Boleto.objects.select_related('reserva', 'reserva__pasajero', 'reserva__vuelo'),
        codigo_barra=codigo
    )

    # Verificación: solo se puede verificar si está emitido y la reserva está confirmada
    puede_verificar = boleto.estado == 'emitido' and boleto.reserva.estado == 'confirmada'

    if request.method == "POST" and puede_verificar:
        boleto.estado = 'verificado'  # o 'confirmado' según tu modelo
        boleto.save()
        messages.success(request, f"Boleto {boleto.codigo_barra} verificado correctamente.")
        return redirect('gestion:lista_boletos_empleado')

    return render(request, 'empleados/boletos/verificar_boleto.html', {
        'boleto': boleto,
        'puede_verificar': puede_verificar,
    })




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



from mail.send import enviar_boleto_por_mail  # Asegurate de que solo reciba "reserva"

from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def ver_asientos(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    vuelo = reserva.vuelo
    asientos = Asiento.objects.filter(avion=vuelo.avion)
    asientos_reserva = reserva.asientos.all()

    # Crear lista de asientos con información ya procesada
    asientos_info = []
    for asiento in asientos:
        tipo_lower = asiento.tipo.lower()  # asegurar coincidencia con PRECIOS_ASIENTO
        precio_asiento = PRECIOS_ASIENTO.get(tipo_lower, Decimal('0.00'))

        asientos_info.append({
            'id': asiento.id,
            'numero': asiento.numero,
            'tipo': asiento.tipo,
            'precio': precio_asiento,
            'ocupado': asiento.estado == 'ocupado' and asiento not in asientos_reserva,
            'es_mio': asiento in asientos_reserva,
        })

    return render(request, 'clientes/reservas/reserva.html', {
        'reserva': reserva,
        'vuelo': vuelo,
        'asientos': asientos_info,
    })



@login_required
@csrf_exempt
def confirmar_compra(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Método no permitido."})

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

            # Crear boleto si no existe
            if not hasattr(reserva, 'boleto'):
                boleto = Boleto.objects.create(
                    reserva=reserva,
                    codigo_barra=f"BOL-{get_random_string(12).upper()}",
                    estado='emitido'
                )
            else:
                boleto = reserva.boleto

        # FUERA de la transacción: enviar correo
        try:
            enviar_boleto_por_mail(reserva)  # <-- solo pasamos "reserva"
            boleto.enviado_por_mail = True
            boleto.save()
        except Exception as e:
            print(f"No se pudo enviar el boleto: {e}")

        return JsonResponse({
            "success": True,
            "total": str(total_precio),
            "reserva_id": reserva.id,
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
    
from django.core.mail import send_mail

def enviar_boleto_por_mail(reserva, boleto):
    subject = f"Boleto de tu reserva #{reserva.id}"
    message = f"Gracias por tu compra. Tu código de boleto es {boleto.codigo_barra}"
    recipient = [reserva.usuario.email]

    send_mail(
        subject,
        message,
        'no-reply@tuaerolinea.com',
        recipient,
        fail_silently=False
    )


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


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages

from .models import Reserva, Boleto
from mail.send import enviar_boleto_por_mail  # ← nuestro módulo mail

@login_required
def ver_boleto(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

    # Crear el boleto si no existe
    boleto = getattr(reserva, 'boleto', None)
    if boleto is None:
        boleto = Boleto.objects.create(
            reserva=reserva,
            codigo_barra=f"BOL-{get_random_string(12).upper()}",
            estado='emitido'
        )

    # Enviar el boleto por mail (solo una vez por visualización)
    if not boleto.enviado_por_mail:
        try:
            enviar_boleto_por_mail(reserva)
            boleto.enviado_por_mail = True
            boleto.save()
            messages.success(request, "Boleto enviado por correo exitosamente.")
        except Exception as e:
            messages.error(request, f"No se pudo enviar el boleto: {e}")

    asientos = list(reserva.asientos.all())
    return render(request, 'clientes/boletos/boleto.html', {
        'reserva': reserva,
        'boleto': boleto,
        'asientos': asientos,
    })

@login_required
def descargar_boleto(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)

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
