from django.contrib import admin
from django.urls import path
#from django.views.generic import TemplateView
from CrudApp.views import PersonasListado, PersonasDetalle, PersonasCrear, PersonasActualizar, PersonasEliminar
#from . import views
 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todas las personas de la Base de Datos
    path('personas/', PersonasListado.as_view(template_name = "personas/index.html"), name='leer'),
   
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una persona
    path('personas/detalle/<int:pk>', PersonasDetalle.as_view(template_name = "personas/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva persona 
    path('personas/crear', PersonasCrear.as_view(template_name = "personas/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una persona o registro de la Base de Datos 
    path('personas/editar/<int:pk>', PersonasActualizar.as_view(template_name = "personas/actualizar.html"), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar una persona o registro de la Base de Datos
    path('personas/eliminar/<int:pk>', PersonasEliminar.as_view(), name='eliminar'),
]