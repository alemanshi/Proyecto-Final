from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from productos.views import home, registro, lista_articulos, carrito, contacto, agregar_al_carrito, eliminar_del_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='register'),
    path('home/', home, name='home'),
]
