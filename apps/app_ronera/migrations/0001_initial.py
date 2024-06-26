# Generated by Django 5.0 on 2024-01-04 21:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Barril",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.BigIntegerField(unique=True, verbose_name="Código")),
                (
                    "inicio",
                    models.DateField(verbose_name="Fecha Inicio de Añejamiento"),
                ),
                (
                    "grado",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Tiene que ser positivo"
                            )
                        ],
                        verbose_name="Grado",
                    ),
                ),
                ("edad", models.PositiveIntegerField(verbose_name="Edad del Barril")),
                (
                    "tipo",
                    models.CharField(max_length=256, verbose_name="Tipo de Material"),
                ),
            ],
            options={
                "verbose_name": "Barril",
                "verbose_name_plural": "Barriles",
            },
        ),
        migrations.CreateModel(
            name="Insumo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256, verbose_name="Nombre")),
                ("cantidad", models.PositiveIntegerField(verbose_name="Cantidad")),
            ],
            options={
                "verbose_name": "Insumo",
                "verbose_name_plural": "Insumos",
            },
        ),
        migrations.CreateModel(
            name="TipoDeCliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=256, verbose_name="Tipo")),
            ],
            options={
                "verbose_name": "Tipo De Cliente",
                "verbose_name_plural": "Tipos De Clientes",
            },
        ),
        migrations.CreateModel(
            name="UnidadDeCosto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Unidad De Costo",
                "verbose_name_plural": "Unidades De Costo",
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256, verbose_name="Nombre")),
                (
                    "precio",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Tiene que ser positivo"
                            )
                        ],
                        verbose_name="Precio",
                    ),
                ),
                ("cantidad", models.PositiveIntegerField(verbose_name="Cantidad")),
                (
                    "insumos",
                    models.ManyToManyField(
                        to="app_ronera.insumo", verbose_name="Insumos"
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
            },
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256, verbose_name="Nombre")),
                ("entidad", models.CharField(max_length=256, verbose_name="Entidad")),
                (
                    "direccion",
                    models.CharField(max_length=500, verbose_name="Dirección"),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_ronera.tipodecliente",
                        verbose_name="Tipo De Cliente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256, verbose_name="Nombre")),
                (
                    "precio",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Tiene que ser positivo"
                            )
                        ],
                        verbose_name="Precio",
                    ),
                ),
                (
                    "grado",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Tiene que ser positivo"
                            )
                        ],
                        verbose_name="Grado",
                    ),
                ),
                ("volumen", models.PositiveIntegerField(verbose_name="Volumen")),
                (
                    "annejamiento",
                    models.CharField(
                        max_length=256, verbose_name="Tiempo de añejamiento"
                    ),
                ),
                (
                    "unidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_ronera.unidaddecosto",
                        verbose_name="Unidad De Costo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
    ]
