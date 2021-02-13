# Generated by Django 2.2.18 on 2021-02-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0005_auto_20210213_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('CheckIn', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('CheckOut', models.CharField(default='DEFAULT VALUE', max_length=100)),
            ],
            options={
                'db_table': 'personas',
            },
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]