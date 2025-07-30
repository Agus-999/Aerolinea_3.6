from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField(default=1)       # Valor por defecto
    columnas = models.PositiveIntegerField(default=1)    # Valor por defecto

    def __str__(self):
        return self.modelo
