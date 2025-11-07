from django.contrib import admin
from .models import Sucursal, Cliente, Empleado

admin.site.register(Sucursal)
admin.site.register(Cliente)  # ¡Ahora sí registrado!
admin.site.register(Empleado)