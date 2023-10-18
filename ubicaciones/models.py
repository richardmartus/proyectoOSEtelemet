from django.db import models

class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45)
    id_region = models.ForeignKey('Regiones', models.DO_NOTHING, db_column='id_region')

    def __str__(self):
        return f"{self.departamento}, {self.id_departamento}"

    class Meta:
        managed = False
        db_table = 'departamentos'



class Localidades(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=45)
    id_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento')

    def __str__(self):
        return f"{self.localidad}"

    class Meta:
        managed = False
        db_table = 'localidades'


class Regiones(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.region}"

    class Meta:
        managed = False
        db_table = 'regiones'


class Sectores(models.Model):
    id_sector = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.sector}"

    class Meta:
        managed = False
        db_table = 'sectores'


class Coordenadas(models.Model):
    localidad = models.ForeignKey(Localidades, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f"{self.localidad}, {self.latitud}, {self.longitud}"

    class Meta:
        db_table = 'coordenadas'