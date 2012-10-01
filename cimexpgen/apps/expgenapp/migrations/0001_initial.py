# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Experiment'
        db.create_table('expgenapp_experiment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('control', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rationale', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('expgenapp', ['Experiment'])

        # Adding M2M table for field requirements on 'Experiment'
        db.create_table('expgenapp_experiment_requirements', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('experiment', models.ForeignKey(orm['expgenapp.experiment'], null=False)),
            ('numericalrequirement', models.ForeignKey(orm['expgenapp.numericalrequirement'], null=False))
        ))
        db.create_unique('expgenapp_experiment_requirements', ['experiment_id', 'numericalrequirement_id'])

        # Adding model 'NumericalRequirement'
        db.create_table('expgenapp_numericalrequirement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docid', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('reqtype', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('expgenapp', ['NumericalRequirement'])

        # Adding model 'RequirementOption'
        db.create_table('expgenapp_requirementoption', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docid', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('expgenapp', ['RequirementOption'])


    def backwards(self, orm):
        # Deleting model 'Experiment'
        db.delete_table('expgenapp_experiment')

        # Removing M2M table for field requirements on 'Experiment'
        db.delete_table('expgenapp_experiment_requirements')

        # Deleting model 'NumericalRequirement'
        db.delete_table('expgenapp_numericalrequirement')

        # Deleting model 'RequirementOption'
        db.delete_table('expgenapp_requirementoption')


    models = {
        'expgenapp.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['expgenapp.NumericalRequirement']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'expgenapp.numericalrequirement': {
            'Meta': {'object_name': 'NumericalRequirement'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'docid': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reqtype': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'expgenapp.requirementoption': {
            'Meta': {'object_name': 'RequirementOption'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'docid': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['expgenapp']