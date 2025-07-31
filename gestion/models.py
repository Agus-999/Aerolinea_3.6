from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField(default=1)       # Valor por defecto
    columnas = models.PositiveIntegerField(default=1)    # Valor por defecto

    def __str__(self):
        return self.modelo


from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField(default=1)
    columnas = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.modelo


class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.fecha_salida.date()})"
