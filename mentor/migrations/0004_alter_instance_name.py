# Generated by Django 4.0.6 on 2022-12-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_alter_instance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
