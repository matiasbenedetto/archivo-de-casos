# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Caso.edad'
        db.alter_column('archivo_caso', 'edad', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    def backwards(self, orm):

        # Changing field 'Caso.edad'
        db.alter_column('archivo_caso', 'edad', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        'archivo.caso': {
            'Meta': {'object_name': 'Caso'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'circunstancias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fecha_deceso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuerza': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imputados': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '1'}),
            'situacion_procesal': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['archivo']