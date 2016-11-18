from django.contrib import admin
from .models import Usuario, Libro, Prestamo, UsuarioAdmin, LibroAdmin

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Prestamo)
