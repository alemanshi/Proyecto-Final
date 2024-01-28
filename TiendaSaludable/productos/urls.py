from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, lista_articulos, carrito, contacto, agregar_al_carrito, eliminar_del_carrito, RegistroUsuario

app_name = 'productos'

urlpatterns = [
    path('articulos/', lista_articulos, name='lista_articulos'),
    path('carrito/', carrito, name='carrito'),
    path('contacto/', contacto, name='contacto'),
    path('', home, name='home'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('login/', auth_views.LoginView.as_view(template_name='productos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='productos:home'), name='logout', kwargs={'next_page': 'productos:home'}),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
]