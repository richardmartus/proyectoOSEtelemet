# Generated by Django 4.2.6 on 2023-10-14 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitud', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicaciones.localidades')),
            ],
            options={
                'db_table': 'coordenadas',
            },
        ),
    ]
