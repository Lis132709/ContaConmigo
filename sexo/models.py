from django.db import models

# Create your models here.

class Sexo(models.Model):
    sexo = models.CharField(max_length=255)

    def __str__(self):
        return f'Sexo: {self.sexo}'
