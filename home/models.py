from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='cliente')

    def __str__(self):
        return f"{self.username} ({self.rol})"
