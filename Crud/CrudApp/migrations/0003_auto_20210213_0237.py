# Generated by Django 2.2.18 on 2021-02-13 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0002_auto_20210213_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='Check_In',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='Nombre',
        ),
    ]
