from django.db import models

# Modelo para la categoría de productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

# Modelo para los clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo para los carritos de compra
class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carritos')
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.cliente.nombre}"

# Modelo para los ítems en el carrito de compra
class ItemCarrito(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='carrito', default=None)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
