# Generated by Django 4.0.6 on 2022-12-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='instance_id',
            new_name='area',
        ),
    ]