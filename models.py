# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

"""
from django.db import models

class Archivodecasos(models.Model):
    numcaso = models.IntegerField(null=True, db_column='NumCaso', blank=True) # Field name made lowercase.
    nombre = models.CharField(max_length=1530, db_column='Nombre', blank=True) # Field name made lowercase.
    edad = models.CharField(max_length=1530, db_column='Edad', blank=True) # Field name made lowercase.
    mayor/menor = models.CharField(max_length=300, db_column='Mayor/Menor', blank=True) # Field name made lowercase.
    cod_edad = models.IntegerField(null=True, db_column='Cod_Edad', blank=True) # Field name made lowercase.
    fecha_de_deceso = models.DateField(null=True, db_column='Fecha de Deceso', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    año = models.IntegerField(null=True, db_column='A\xc3\xb1o', blank=True) # Field name made lowercase.
    ciudad = models.CharField(max_length=300, db_column='Ciudad', blank=True) # Field name made lowercase.
    cod_provincia = models.IntegerField(null=True, db_column='Cod_Provincia', blank=True) # Field name made lowercase.
    provincia = models.CharField(max_length=1530, db_column='Provincia', blank=True) # Field name made lowercase.
    imputados = models.CharField(max_length=1530, db_column='Imputados', blank=True) # Field name made lowercase.
    cod_fuerza = models.CharField(max_length=300, db_column='Cod_Fuerza', blank=True) # Field name made lowercase.
    situación_procesal = models.TextField(db_column='Situaci\xc3\xb3n Procesal', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    circunstancias = models.TextField(db_column='Circunstancias', blank=True) # Field name made lowercase.
    cod_circunstancia = models.IntegerField(null=True, db_column='Cod_Circunstancia', blank=True) # Field name made lowercase.
    num = models.IntegerField(null=True, db_column='NUM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ArchivodeCasos'

"""