# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fuerza'
        db.create_table('archivo_fuerza', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('archivo', ['Fuerza'])

        # Adding model 'Circunstancia'
        db.create_table('archivo_circunstancia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('archivo', ['Circunstancia'])

        # Adding model 'Caso'
        db.create_table('archivo_caso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('edad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(default='V', max_length=1)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha_deceso', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
            ('imputados', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('situacion_procesal', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('circunstancia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archivo.Circunstancia'], null=True)),
            ('circunstancias', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mayor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fuerza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archivo.Fuerza'])),
        ))
        db.send_create_signal('archivo', ['Caso'])

        # Adding model 'Archivodecasos'
        db.create_table(u'ArchivodeCasos', (
            ('numcaso', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='NumCaso')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=1530, db_column='Nombre', blank=True)),
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=1530, db_column='Edad', blank=True)),
            ('mayor', self.gf('django.db.models.fields.CharField')(max_length=300, db_column='Mayor', blank=True)),
            ('cod_edad', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='Cod_Edad', blank=True)),
            ('fecha_de_deceso', self.gf('django.db.models.fields.DateField')(null=True, db_column='Fecha de Deceso', blank=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='Anio', blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=300, db_column='Ciudad', blank=True)),
            ('cod_provincia', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='Cod_Provincia', blank=True)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=1530, db_column='Provincia', blank=True)),
            ('imputados', self.gf('django.db.models.fields.CharField')(max_length=1530, db_column='Imputados', blank=True)),
            ('cod_fuerza', self.gf('django.db.models.fields.CharField')(max_length=300, db_column='Cod_Fuerza', blank=True)),
            ('situacion_procesal', self.gf('django.db.models.fields.TextField')(db_column='Situacion Procesal', blank=True)),
            ('circunstancias', self.gf('django.db.models.fields.TextField')(db_column='Circunstancias', blank=True)),
            ('cod_circunstancia', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='Cod_Circunstancia', blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='NUM', blank=True)),
        ))
        db.send_create_signal('archivo', ['Archivodecasos'])


    def backwards(self, orm):
        # Deleting model 'Fuerza'
        db.delete_table('archivo_fuerza')

        # Deleting model 'Circunstancia'
        db.delete_table('archivo_circunstancia')

        # Deleting model 'Caso'
        db.delete_table('archivo_caso')

        # Deleting model 'Archivodecasos'
        db.delete_table(u'ArchivodeCasos')


    models = {
        'archivo.archivodecasos': {
            'Meta': {'object_name': 'Archivodecasos', 'db_table': "u'ArchivodeCasos'"},
            'anio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'Anio'", 'blank': 'True'}),
            'circunstancias': ('django.db.models.fields.TextField', [], {'db_column': "'Circunstancias'", 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'Ciudad'", 'blank': 'True'}),
            'cod_circunstancia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'Cod_Circunstancia'", 'blank': 'True'}),
            'cod_edad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'Cod_Edad'", 'blank': 'True'}),
            'cod_fuerza': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'Cod_Fuerza'", 'blank': 'True'}),
            'cod_provincia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'Cod_Provincia'", 'blank': 'True'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '1530', 'db_column': "'Edad'", 'blank': 'True'}),
            'fecha_de_deceso': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'Fecha de Deceso'", 'blank': 'True'}),
            'imputados': ('django.db.models.fields.CharField', [], {'max_length': '1530', 'db_column': "'Imputados'", 'blank': 'True'}),
            'mayor': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'Mayor'", 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '1530', 'db_column': "'Nombre'", 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'NUM'", 'blank': 'True'}),
            'numcaso': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'NumCaso'"}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '1530', 'db_column': "'Provincia'", 'blank': 'True'}),
            'situacion_procesal': ('django.db.models.fields.TextField', [], {'db_column': "'Situacion Procesal'", 'blank': 'True'})
        },
        'archivo.caso': {
            'Meta': {'object_name': 'Caso'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'circunstancia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archivo.Circunstancia']", 'null': 'True'}),
            'circunstancias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_deceso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fuerza': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archivo.Fuerza']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imputados': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mayor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'V'", 'max_length': '1'}),
            'situacion_procesal': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'archivo.circunstancia': {
            'Meta': {'object_name': 'Circunstancia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'archivo.fuerza': {
            'Meta': {'object_name': 'Fuerza'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['archivo']