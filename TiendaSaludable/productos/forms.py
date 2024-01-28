from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Cliente, ItemCarrito

# Formulario para crear/editar un producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'disponible', 'categoria']

# Formulario para crear/editar un cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

# Formulario de búsqueda
class BuscarForm(forms.Form):
    busqueda = forms.CharField(label='Buscar')

# Formulario para agregar un producto al carrito
class CarritoForm(forms.Form):
    producto_id = forms.IntegerField()
    cantidad = forms.IntegerField(min_value=1)

# Formulario para crear/editar un ítem en el carrito
class ItemCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'cantidad']

# Formulario de contacto
class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='E-mail')

    # Opciones para el motivo del contacto
    opciones_motivo = [
        ('consultas', 'Consultas'),
        ('reclamos', 'Reclamos'),
        ('promociones', 'Recibir Promociones'),
    ]

    motivo = forms.ChoiceField(label='Motivo', choices=opciones_motivo)
    comentarios = forms.CharField(label='Comentarios', widget=forms.Textarea)

# Formulario de registro de usuario
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Apellido')
    email = forms.EmailField(required=True, help_text='Email')
    telefono = forms.CharField(max_length=15, required=False, help_text='Teléfono')
    avatar = forms.ImageField(required=False, help_text='Foto de perfil')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'telefono', 'avatar',)
