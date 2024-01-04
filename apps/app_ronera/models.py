from django.db import models
from apps.users.models import *
from django.core.validators import MaxValueValidator,MinValueValidator
import datetime
from django.core.exceptions import ValidationError
# Create your models here.


class Insumo(models.Model):
    class Meta:
        verbose_name="Insumo"
        verbose_name_plural="Insumos"
    nombre = models.CharField(verbose_name="Nombre",max_length=256)
    cantidad=models.PositiveIntegerField(verbose_name="Cantidad")
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    nombre = models.CharField(verbose_name="Nombre",max_length=256)
    precio = models.FloatField(verbose_name="Precio",validators=[
            MinValueValidator(0,message="Tiene que ser positivo")
        ])
    cantidad=models.PositiveIntegerField(verbose_name="Cantidad")
    insumos = models.ManyToManyField(Insumo, verbose_name="Insumos")

    def __str__(self):
        return self.nombre

class Barril(models.Model):
    class Meta:
        verbose_name="Barril"
        verbose_name_plural="Barriles"
    codigo=models.BigIntegerField(verbose_name="Código",unique=True)
    inicio=models.DateField(verbose_name="Fecha Inicio de Añejamiento")
    grado=models.FloatField(verbose_name="Grado",validators=[
            MinValueValidator(0,message="Tiene que ser positivo")
        ])
    edad = models.PositiveIntegerField(verbose_name="Edad del Barril")
    tipo=models.CharField(verbose_name="Tipo de Material",max_length=256)


    def __str__(self):
        return str(self.codigo)

class UnidadDeCosto(models.Model):
    class Meta:
        verbose_name="Unidad De Costo"
        verbose_name_plural="Unidades De Costo"
    nombre = models.CharField(verbose_name="Nombre",max_length=256)
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    class Meta:
        verbose_name="Marca"
        verbose_name_plural="Marcas"
    nombre = models.CharField(verbose_name="Nombre",max_length=256)
    precio = models.FloatField(verbose_name="Precio",validators=[
            MinValueValidator(0,message="Tiene que ser positivo")
        ])
    grado = models.FloatField(verbose_name="Grado", validators=[
        MinValueValidator(0, message="Tiene que ser positivo")
    ])
    volumen=models.PositiveIntegerField(verbose_name="Volumen")
    annejamiento=models.CharField(verbose_name="Tiempo de añejamiento",max_length=256)
    unidad = models.ForeignKey(UnidadDeCosto, verbose_name="Unidad De Costo", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class TipoDeCliente(models.Model):
    class Meta:
        verbose_name = "Tipo De Cliente"
        verbose_name_plural = "Tipos De Clientes"

    tipo = models.CharField(verbose_name="Tipo", max_length=256)
    def __str__(self):
        return self.tipo



class Cliente(models.Model):
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
    nombre = models.CharField(verbose_name="Nombre",max_length=256)
    entidad = models.CharField(verbose_name="Entidad", max_length=256)
    direccion = models.CharField(verbose_name="Dirección", max_length=500)
    tipo = models.ForeignKey(TipoDeCliente, verbose_name="Tipo De Cliente", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre