from django.contrib import admin
from .models import *
# Register your models here.




class InsumoAdmin(admin.ModelAdmin):
    model = Insumo
    list_display = ('nombre', 'cantidad',)
    search_fields = ('nombre', 'cantidad',)
    ordering = ('nombre', 'cantidad',)
admin.site.register(Insumo,InsumoAdmin)

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('nombre', 'precio','cantidad')
    search_fields = ('nombre', 'precio','cantidad')
    ordering = ('nombre', 'precio','cantidad')
    filter_horizontal = ('insumos',)
admin.site.register(Producto,ProductoAdmin)

class BarrilAdmin(admin.ModelAdmin):
    model = Barril
    list_display = ('codigo', 'grado','edad','tipo',)
    search_fields = ('codigo', 'grado','edad','tipo',)
    list_filter = ('edad','tipo',)
    ordering = ('codigo', 'grado','edad','tipo',)
    date_hierarchy = 'inicio'
admin.site.register(Barril,BarrilAdmin)

class UnidadDeCostoAdmin(admin.ModelAdmin):
    model = UnidadDeCosto
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
admin.site.register(UnidadDeCosto,UnidadDeCostoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    model = Marca
    list_display = ('nombre', 'precio', 'grado','volumen','unidad','annejamiento',)
    search_fields = ('nombre', 'precio', 'grado','volumen','unidad','annejamiento',)
    ordering = ('nombre', 'precio', 'grado','volumen','unidad','annejamiento',)
    list_filter = ('unidad','annejamiento',)
admin.site.register(Marca,MarcaAdmin)

class TipoDeClienteAdmin(admin.ModelAdmin):
    model = TipoDeCliente
    list_display = ('tipo',)
    search_fields = ('tipo',)
    ordering = ('tipo',)
admin.site.register(TipoDeCliente,TipoDeClienteAdmin)

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('nombre', 'entidad', 'tipo',)
    search_fields = ('nombre', 'entidad', 'tipo',)
    ordering = ('nombre', 'entidad', 'tipo',)
    list_filter = ('entidad','tipo',)
admin.site.register(Cliente,ClienteAdmin)