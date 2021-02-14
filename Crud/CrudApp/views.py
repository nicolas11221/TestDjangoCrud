# Instanciamos el modelo para poder usarlo en nuestras Vistas CRUD
from .models import Personas
from django.shortcuts import render
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
# Habilitamos los formularios en Django
from django import forms

from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PersonasListado(ListView):
    model = Personas
 
class PersonasDetalle(DetailView):
    model = Personas
 
class PersonasCrear(SuccessMessageMixin, CreateView):
    model = Personas
    form = Personas
    fields = "__all__"
    success_message = 'Persona Creado Correctamente !' # Mostramos este Mensaje luego de Crear una persona
 
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
      return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class PersonasActualizar(SuccessMessageMixin, UpdateView):
    model = Personas
    form = Personas
    fields = "__all__"
    success_message = 'Persona Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar una persona
 
    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class PersonasEliminar(SuccessMessageMixin, DeleteView):
    model = Personas
    form = Personas
    fields = "__all__"
 
    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self):
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una persona
        messages.success (self.request, (success_message))
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


