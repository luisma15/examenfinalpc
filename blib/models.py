
from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Libro(models.Model):
    li_ISBN = models.CharField(max_length = 13)
    li_Titulo = models.CharField(max_length = 20)
    #li_Portada = models.ImageField(upload_to='imagen/')
    li_Autor = models.CharField(max_length = 20)
    li_Editorial = models.CharField(max_length = 20)
    li_Pais = models.CharField(max_length = 15)
    li_anio = models.CharField(max_length = 6)

    def __str__(self):
        return self.li_Titulo

class Usuario(models.Model):
    us_Nombre = models.CharField(max_length = 20)
    us_DPI = models.CharField(max_length = 13)


    def __str__(self):
        return self.us_Nombre

class Prestamo(models.Model):
    pres_FechaPrestamo = models.DateTimeField(default = timezone.now)
    pres_FechaDevolucionPropuesta = models.DateTimeField()
    pres_FechaDevolucionReal = models.DateTimeField()
    pres_Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    pres_Libros=models.ForeignKey(Libro,on_delete=models.CASCADE)



class PrestamoInLine(admin.TabularInline):
    model = Prestamo
    extra = 1

class LibroAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)
