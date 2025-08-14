from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from decimal import Decimal

PRECIOS_ASIENTO = {
    'economico': Decimal('100.00'),
    'premium': Decimal('200.00'),
    'ejecutivo': Decimal('300.00'),
    'primera': Decimal('400.00'),
}

def enviar_boleto_por_mail(reserva):
    """
    Envía el boleto por correo electrónico al pasajero.
    Incluye todos los datos de reserva, vuelo, pasajero y asientos con sus precios.
    Funciona con Mailtrap y maneja posibles errores de email faltante.
    """
    # Validar que haya email
    email_destino = getattr(reserva.pasajero, 'email', None)
    if not email_destino:
        print("No se puede enviar el boleto: el pasajero no tiene email.")
        return

    # Obtener boleto y asientos
    boleto = getattr(reserva, 'boleto', None)
    if boleto is None:
        print("No se puede enviar el boleto: no existe un boleto asociado a la reserva.")
        return

    vuelo = reserva.vuelo
    pasajero = reserva.pasajero
    asientos = reserva.asientos.all()

    # Preprocesar asientos con precios
    asientos_info = []
    for asiento in asientos:
        tipo_lower = asiento.tipo.lower()  # asegurar coincidencia con PRECIOS_ASIENTO
        precio_asiento = PRECIOS_ASIENTO.get(tipo_lower, Decimal('0.00'))
        asientos_info.append({
            'numero': asiento.numero,
            'tipo': asiento.tipo,
            'precio': precio_asiento,
        })

    # Crear asunto usando código de vuelo o ID
    vuelo_identificador = getattr(vuelo, 'codigo_vuelo', f"#{vuelo.id}")
    subject = f"Boleto de Vuelo {vuelo_identificador}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [email_destino]

    try:
        # Renderizar contenido HTML completo
        html_content = render_to_string('clientes/boletos/boleto_email.html', {
            'reserva': reserva,
            'boleto': boleto,
            'asientos': asientos_info,
            'vuelo': vuelo,
            'pasajero': pasajero,
        })

        # Texto plano como fallback
        plain_text = f"""
Gracias por tu compra.

Código de boleto: {boleto.codigo_barra}
Pasajero: {pasajero.nombre} ({pasajero.documento})
Vuelo: {vuelo_identificador}
Fecha de vuelo: {getattr(vuelo, 'fecha', 'N/A')}
Asientos: {', '.join([f'{a.numero} ({PRECIOS_ASIENTO.get(a.tipo.lower(), 0.00)})' for a in asientos])}
Total: ${reserva.precio}
"""

        # Enviar email HTML
        msg = EmailMultiAlternatives(subject, plain_text, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print(f"Boleto enviado correctamente a {email_destino}")

    except Exception as e:
        print(f"No se pudo enviar el boleto: {e}")
