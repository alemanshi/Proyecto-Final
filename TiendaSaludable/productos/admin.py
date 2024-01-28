from django.contrib import admin
from .models import Producto, Cliente, ItemCarrito, Categoria

# Define las clases de administración personalizadas si es necesario
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'subtotal')
    list_filter = ('cliente',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

# Registra los modelos en la interfaz de administración de Django
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
