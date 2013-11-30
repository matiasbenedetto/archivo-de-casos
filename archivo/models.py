#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.db import models
from geoposition.fields import GeopositionField


class Fuerza (models.Model):

    def __unicode__(self):
        return self.nombre

    #tipo =  #nacional, provincial, municipal, privada
    nombre = models.CharField(max_length=30)


class Circunstancia (models.Model):

    def __unicode__(self):
        return self.nombre

    nombre = models.CharField(max_length=60)

class TipoEdad (models.Model):
    def __unicode__(self):
        return self.nombre

    nombre = models.CharField(max_length=60)


class Caso (models.Model):
    def __unicode__(self):
        return self.nombre

    SEXOS =(
            ('V', 'Varon'),
            ('M', 'Mujer')
            ) 
    
    apellido = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField(blank=True, null=True)
    tipo_edad = models. ForeignKey(TipoEdad, null=True, default=None)
    mayor = models.CharField(max_length=255, null=True, default=None)
    sexo = models.CharField(max_length=1, choices=SEXOS, default='V')
    ciudad = models.CharField(max_length=255, null=True)
    provincia = models.CharField(max_length=255)
    fecha_deceso = models.DateField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    imputados = models.TextField(blank=True)
    situacion_procesal = models.TextField(blank=True)
    circunstancia = models. ForeignKey(Circunstancia, null=True, default=None)
    circunstancias = models.TextField(blank=True)
    mayor = models.CharField(max_length=255)
    fuerza = models. ForeignKey(Fuerza)
    coordenadas = GeopositionField()
    


"""    
class Gobierno (models.Model):
    nombre =   #nombre de la figura maxima, presidente, gobernador
    tipo =     # nacional, provincial
    inicio =   #cuando empezo el mandato
    termino =   #cuando termino el gobierno

"""

class Archivodecasos(models.Model):
    numcaso = models.IntegerField(db_column='NumCaso', primary_key=True) # Field name made lowercase.
    nombre = models.CharField(max_length=1530, db_column='Nombre', blank=True) # Field name made lowercase.
    edad = models.CharField(max_length=1530, db_column='Edad', blank=True) # Field name made lowercase.
    mayor = models.CharField(max_length=300, db_column='Mayor', blank=True) # Field name made lowercase.
    cod_edad = models.IntegerField(null=True, db_column='Cod_Edad', blank=True) # Field name made lowercase.
    fecha_de_deceso = models.DateField(null=True, db_column='Fecha de Deceso', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    anio = models.IntegerField(null=True, db_column='Anio', blank=True) # Field name made lowercase.
    ciudad = models.CharField(max_length=300, db_column='Ciudad', blank=True) # Field name made lowercase.
    cod_provincia = models.IntegerField(null=True, db_column='Cod_Provincia', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=1530, db_column='Provincia', blank=True) # Field name made lowercase.
    imputados = models.CharField(max_length=1530, db_column='Imputados', blank=True) # Field name made lowercase.
    cod_fuerza = models.CharField(max_length=300, db_column='Cod_Fuerza', blank=True) # Field name made lowercase.
    situacion_procesal = models.TextField(db_column='Situacion Procesal', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    circunstancias = models.TextField(db_column='Circunstancias', blank=True) # Field name made lowercase.
    cod_circunstancia = models.IntegerField(null=True, db_column='Cod_Circunstancia', blank=True) # Field name made lowercase.
    num = models.IntegerField(null=True, db_column='NUM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ArchivodeCasos'
