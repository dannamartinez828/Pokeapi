from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=255)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    ataque1 = models.CharField(max_length=50)
    ataque2 = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
