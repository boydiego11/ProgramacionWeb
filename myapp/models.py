from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    username = models.CharField(max_length=255, unique=True, verbose_name='nombre de usuario')
    password = models.CharField(max_length=255, verbose_name='contraseña')
    email = models.EmailField(max_length=255, unique=True, verbose_name='correo electrónico')
    birth_date = models.DateField(verbose_name='fecha de nacimiento')
    shipping_address = models.TextField(verbose_name='dirección de despacho')
    # Define los roles de usuario aquí
    ROL_CHOICES = (
        ('usuario_normal', 'Usuario Normal'),
        ('administrador', 'Administrador'),
    )
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def _str_(self):
        return f"{self.username} ({self.email})"
   


class Usuario(AbstractUser):
    # Otros campos de tu modelo

    # Cambia el related_name para evitar conflictos con los accesos inversos de auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_related',  # Cambia 'usuarios_related' por el nombre que prefieras
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_related',  # Cambia 'usuarios_related' por el nombre que prefieras
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

