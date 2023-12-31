# Generated by Django 4.2.6 on 2023-10-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'regiones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('id_sector', models.AutoField(primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sectores',
                'managed': False,
            },
        ),
    ]
