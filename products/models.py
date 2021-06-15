from django.db import models
## Comentario para borrar
"""
Para hacer un foreing key a el usuario del sistema, tienen que importar el usuario:
Opción 1>
from django.contrib.auth import get_user_model
user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

Opción 2>
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

Traer de otra otra app un modelo>
from applicacion.models import Modelo
"""

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nombre', max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Categoría padre', 
                                blank=True, null=True, default=None)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Categoría'
        verbose_name_plural= 'Categorías'


class Product(models.Model):
    name = models.CharField('Nombre', max_length=256)
    unit_price = models.FloatField('Precio Unitario')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'
