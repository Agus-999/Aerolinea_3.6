from django.db import models
from home.models import Usuario  # Importamos tu modelo personalizado

# ----------------------------
# AVION
# ----------------------------
class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField(default=1)
    columnas = models.PositiveIntegerField(default=1)
    imagen = models.ImageField(upload_to='aviones/', null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.capacidad != self.filas * self.columnas:
            raise ValidationError("La capacidad debe coincidir con filas × columnas.")
        
    def __str__(self):
        return self.modelo

# ----------------------------
# VUELO
# ----------------------------
class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE, related_name='vuelos')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.DurationField(blank=True, null=True)

    ESTADO_CHOICES = [
        ('programado', 'Programado'),
        ('en_vuelo', 'En Vuelo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    gestionado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida.date()})"

# ----------------------------
# PASAJERO
# ----------------------------
from django.db import models
from django.conf import settings

class Pasajero(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pasajero',
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, blank=True)  # ← permite nulos
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo_documento = models.CharField(
        max_length=20,
        choices=[
            ('dni', 'DNI'),
            ('pasaporte', 'Pasaporte'),
            ('otro', 'Otro')
        ],
        null=True, blank=True
    )

    def __str__(self):
        return self.nombre


    
# ----------------------------
# ASIENTO
# ----------------------------
class Asiento(models.Model):
    class Meta:
        unique_together = ('avion', 'numero', 'fila', 'columna')

    avion = models.ForeignKey(Avion, on_delete=models.CASCADE, related_name='asientos')
    numero = models.CharField(max_length=5)
    fila = models.IntegerField()
    columna = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=[
        ('economico', 'Económico'),
        ('premium', 'Premium Economy'),
        ('ejecutivo', 'Ejecutivo'),
        ('primera', 'Primera Clase'),
    ])
    estado = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado')
    ])
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Asiento {self.numero} - F{self.fila}C{self.columna}"

# ----------------------------
# RESERVA
# ----------------------------
from django.db import transaction

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ]

    vuelo = models.ForeignKey('Vuelo', on_delete=models.CASCADE, related_name='reservas')
    pasajero = models.ForeignKey('Pasajero', on_delete=models.CASCADE, related_name='reservas')

    # Relación muchos a muchos para varios asientos
    asientos = models.ManyToManyField('Asiento', related_name='reservas', blank=True)

    # Relación con el usuario autenticado (usa el modelo configurado en AUTH_USER_MODEL)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)

    codigo_reserva = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.pasajero.nombre}"

    def asientos_str(self):
        """Devuelve una lista de asientos como texto."""
        return ", ".join([str(asiento) for asiento in self.asientos.all()])
    
    def liberar_asientos(self):
            """Marca como disponibles todos los asientos de la reserva y limpia la M2M."""
            with transaction.atomic():
                for asiento in self.asientos.select_for_update():
                    asiento.estado = 'disponible'
                    asiento.save(update_fields=['estado'])
                self.asientos.clear()

    def delete(self, *args, **kwargs):
        """Al eliminar la reserva, asegurate de liberar los asientos primero."""
        with transaction.atomic():
            self.liberar_asientos()
            super().delete(*args, **kwargs)
            
# ----------------------------
# BOLETO
# ----------------------------
class Boleto(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='boleto')
    codigo_barra = models.CharField(max_length=100, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('emitido', 'Emitido'),
            ('cancelado', 'Cancelado'),
            ('verificado', 'Verificado')  # ← nuevo estado
        ],
        default='emitido'
    )
    enviado_por_mail = models.BooleanField(default=False)  # ← nuevo campo

    def __str__(self):
        return f"Boleto {self.codigo_barra} - {self.reserva.codigo_reserva}"
