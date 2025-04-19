from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import random
from datetime import datetime, timedelta
from .models import (
    Insumo, Producto, Barril, UnidadDeCosto, 
    Marca, TipoDeCliente, Cliente
)
User=get_user_model()
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'apps.app_ronera':
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='123',
                email='admin@example.com',
                first_name='admin',
                last_name='admin'
            )

        # Crear Unidades de Costo
        unidades = ['Litro', 'Kilogramo', 'Unidad']
        for unidad in unidades:
            UnidadDeCosto.objects.get_or_create(nombre=unidad)

        # Crear Tipos de Cliente
        tipos_cliente = ['Minorista', 'Mayorista', 'Distribuidor']
        for tipo in tipos_cliente:
            TipoDeCliente.objects.get_or_create(tipo=tipo)

        # Crear Insumos
        insumos = ['Azúcar', 'Levadura', 'Agua', 'Colorante', 'Saborizante']
        for insumo in insumos:
            Insumo.objects.get_or_create(
                nombre=insumo,
                cantidad=random.randint(100, 1000)
            )

        # Crear Barriles
        tipos_barril = ['Roble Americano', 'Roble Francés', 'Roble Español']
        start_date = datetime.now() - timedelta(days=5*365)  # 5 años atrás
        end_date = datetime.now()
        
        for i in range(10):
            Barril.objects.get_or_create(
                codigo=random.randint(1000, 9999),
                inicio=random_date(start_date, end_date).date(),
                grado=random.uniform(35, 50),
                edad=random.randint(1, 5),
                tipo=random.choice(tipos_barril)
            )

        # Crear Marcas
        nombres_marcas = ['Ron Añejo', 'Ron Premium', 'Ron Especial']
        for nombre in nombres_marcas:
            Marca.objects.get_or_create(
                nombre=nombre,
                precio=random.uniform(100, 1000),
                grado=random.uniform(35, 50),
                volumen=random.randint(700, 1000),
                annejamiento=f"{random.randint(1, 12)} años",
                unidad=UnidadDeCosto.objects.get(nombre='Litro')
            )

        # Crear Productos
        nombres_productos = ['Ron Clásico', 'Ron Reserva', 'Ron Extra', 'Ron Premium', 'Ron Especial']
        for nombre in nombres_productos:
            producto = Producto.objects.create(
                nombre=nombre,
                precio=random.uniform(50, 500),
                cantidad=random.randint(10, 100)
            )
            # Asignar insumos aleatorios al producto
            insumos_aleatorios = random.sample(list(Insumo.objects.all()), random.randint(1, 3))
            producto.insumos.set(insumos_aleatorios)

        # Crear Clientes
        nombres_empresas = [
            'Distribuidora Central', 'Bebidas del Caribe', 'Licores Premium',
            'Importadora Nacional', 'Exportadora Internacional', 'Comercializadora Local',
            'Mayorista Regional', 'Minorista Express', 'Distribuidora Global',
            'Comercializadora Nacional'
        ]
        estados = ['Ciudad de México', 'Jalisco', 'Nuevo León', 'Puebla', 'Veracruz']
        for nombre in nombres_empresas:
            Cliente.objects.get_or_create(
                nombre=nombre,
                entidad=random.choice(estados),
                direccion=f"Calle {random.randint(1, 100)} #{random.randint(1, 1000)}",
                tipo=TipoDeCliente.objects.order_by('?').first()
            ) 