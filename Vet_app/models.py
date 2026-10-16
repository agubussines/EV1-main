from django.db import models

# Create your models here.
<<<<<<< HEAD
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    # Relación 1:N (ForeignKey): Un usuario tiene muchas mascotas, una mascota pertenece a un usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=30)
    sexo = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
=======
>>>>>>> 96dd9e8b874e2b731393b3b765924d45f58a6fd2
