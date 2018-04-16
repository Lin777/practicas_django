from django.contrib import admin
from .models import Language

#Esto sirve para poder administrar Language desde el Administrador
admin.site.register(Language)