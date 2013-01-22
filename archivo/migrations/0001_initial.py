# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Caso'
        db.create_table('archivo_caso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_deceso', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('imputados', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('situacion_procesal', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('circunstancias', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fuerza', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('archivo', ['Caso'])


    def backwards(self, orm):
        
        # Deleting model 'Caso'
        db.delete_table('archivo_caso')


    models = {
        'archivo.caso': {
            'Meta': {'object_name': 'Caso'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'circunstancias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_deceso': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'fuerza': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imputados': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'situacion_procesal': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['archivo']
