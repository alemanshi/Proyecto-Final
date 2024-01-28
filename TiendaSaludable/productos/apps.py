# django.apps importa la clase AppConfig para la configuración de la aplicación
from django.apps import AppConfig

# Definición de la clase de configuración para la aplicación 'productos'
class ProductosConfig(AppConfig):
    # Configuración del campo de autoincremento para las claves primarias
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación
    name = 'productos'
