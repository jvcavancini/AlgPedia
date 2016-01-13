# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Implementation.date'
        db.add_column(u'algorithm_implementation', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2016, 1, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Interest.date'
        db.add_column(u'algorithm_interest', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2016, 1, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'UserQuestionAnswer.date'
        db.add_column(u'algorithm_userquestionanswer', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2016, 1, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'ImplementationQuestionAnswer.date'
        db.add_column(u'algorithm_implementationquestionanswer', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2016, 1, 13, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Implementation.date'
        db.delete_column(u'algorithm_implementation', 'date')

        # Deleting field 'Interest.date'
        db.delete_column(u'algorithm_interest', 'date')

        # Deleting field 'UserQuestionAnswer.date'
        db.delete_column(u'algorithm_userquestionanswer', 'date')

        # Deleting field 'ImplementationQuestionAnswer.date'
        db.delete_column(u'algorithm_implementationquestionanswer', 'date')


    models = {
        u'algorithm.algorithm': {
            'Meta': {'object_name': 'Algorithm'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 13, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reputation': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['algorithm.Tag']", 'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'algorithm.classification': {
            'Meta': {'ordering': "['name']", 'object_name': 'Classification'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'algorithm.classificationproeficiencyscale': {
            'Meta': {'object_name': 'ClassificationProeficiencyScale', '_ormbases': [u'algorithm.ProeficiencyScale']},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']"}),
            u'proeficiencyscale_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.ProeficiencyScale']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.implementation': {
            'Meta': {'object_name': 'Implementation'},
            'accumulated_weight': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'algorithm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'implementation_set'", 'to': u"orm['algorithm.Algorithm']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ProgrammingLanguage']"}),
            'reputation': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'algorithm.implementationquestion': {
            'Meta': {'object_name': 'ImplementationQuestion', '_ormbases': [u'algorithm.Question']},
            u'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.implementationquestionanswer': {
            'Meta': {'object_name': 'ImplementationQuestionAnswer'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implementation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Implementation']"}),
            'implementation_question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ImplementationQuestion']"}),
            'question_option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.QuestionOption']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'algorithm.interest': {
            'Meta': {'object_name': 'Interest'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Classification']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'algorithm.proeficiencyscale': {
            'Meta': {'object_name': 'ProeficiencyScale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'algorithm.programminglanguage': {
            'Meta': {'object_name': 'ProgrammingLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'algorithm.programminglanguageproeficiencyscale': {
            'Meta': {'object_name': 'ProgrammingLanguageProeficiencyScale', '_ormbases': [u'algorithm.ProeficiencyScale']},
            u'proeficiencyscale_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.ProeficiencyScale']", 'unique': 'True', 'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ProgrammingLanguage']"})
        },
        u'algorithm.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'algorithm.questionoption': {
            'Meta': {'object_name': 'QuestionOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questionoption_set'", 'to': u"orm['algorithm.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'algorithm.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'algorithm.universityrank': {
            'Meta': {'ordering': "['position']", 'object_name': 'UniversityRank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        u'algorithm.userquestion': {
            'Meta': {'object_name': 'UserQuestion', '_ormbases': [u'algorithm.Question']},
            u'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['algorithm.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'algorithm.userquestionanswer': {
            'Meta': {'object_name': 'UserQuestionAnswer'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2016, 1, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.QuestionOption']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.UserQuestion']"})
        },
        u'algorithm.userreputation': {
            'Meta': {'object_name': 'UserReputation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reputation': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.UniversityRank']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['algorithm']