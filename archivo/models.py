from django.db import models

# Create your models here.

class Caso (models.Model):
    SEXOS =(
            ('V', 'Varon'),
            ('M', 'Mujer')
            ) 
    
    apellido = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField(blank=True, null=True) #-1 mayor, -2 menor
    sexo = models.CharField(max_length=1, choices=SEXOS, default='V')
    ciudad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    fecha_deceso = models.DateField(blank=True, null=True)
    imputados = models.TextField(blank=True)
    situacion_procesal = models.TextField(blank=True)
    circunstancias = models.TextField(blank=True)
    fuerza = models.TextField(blank=True)
    #link = 
    #imagenes = 
    
"""
class Fuerza (models.Model):
    tipo =  #nacional, provincial, municipal, privada
    nombre =  
    
class Gobierno (models.Model):
    nombre =   #nombre de la figura maxima, presidente, gobernador
    tipo =     # nacional, provincial
    inicio =   #cuando empezo el mandato
    termino =   #cuando termino el gobierno
    
    
    
    
#como determinan la fuerza ?
#como determinan el gobierno ?
"""