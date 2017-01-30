# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-26 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    def remove_inactive_fields(apps, schema_editor):
        ContactField = apps.get_model('contacts', "ContactField")

        deleted, inactive = ContactField.objects.filter(is_active=False).delete()

        print "Deleted %d inactive fields" % deleted


    dependencies = [
        ('contacts', '0014_install_triggers'),
    ]

    operations = [
        migrations.RunPython(remove_inactive_fields)
    ]
