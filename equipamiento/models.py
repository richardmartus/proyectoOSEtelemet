from django.db import models


class Gateway(models.Model):
    gateway_id = models.AutoField(db_column='GATEWAY_ID', primary_key=True)  # Field name made lowercase.
    gateway_address = models.CharField(db_column='GATEWAY_ADDRESS', unique=True, max_length=8)  # Field name made lowercase.
    gateway_nombre = models.CharField(db_column='GATEWAY_NOMBRE', unique=True, max_length=16)  # Field name made lowercase.
    gateway_latitud = models.CharField(db_column='GATEWAY_LATITUD', max_length=25)  # Field name made lowercase.
    gateway_longitud = models.CharField(db_column='GATEWAY_LONGITUD', max_length=25)  # Field name made lowercase.
    gateway_ubicacion = models.CharField(db_column='GATEWAY_UBICACION', max_length=100)  # Field name made lowercase.
    gateway_ntrasmisiones = models.IntegerField(db_column='GATEWAY_NTRASMISIONES')  # Field name made lowercase.
    gateway_nactividad = models.IntegerField(db_column='GATEWAY_NACTIVIDAD')  # Field name made lowercase.
    gateway_nfalla = models.IntegerField(db_column='GATEWAY_NFALLA')  # Field name made lowercase.
    gateway_password = models.CharField(db_column='GATEWAY_PASSWORD', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gateway'


class MarcasMedidores(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'marcas_medidores'


class ModelosMedidores(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'modelos_medidores'


class Modulo(models.Model):
    modulo_id = models.AutoField(db_column='MODULO_ID', primary_key=True)  # Field name made lowercase.
    modulo_address = models.CharField(db_column='MODULO_ADDRESS', unique=True, max_length=8)  # Field name made lowercase.
    modulo_tipo = models.IntegerField(db_column='MODULO_TIPO')  # Field name made lowercase.
    modulo_factor = models.FloatField(db_column='MODULO_FACTOR', blank=True, null=True)  # Field name made lowercase.
    modulo_calle = models.CharField(db_column='MODULO_CALLE', max_length=100)  # Field name made lowercase.
    modulo_numero = models.CharField(db_column='MODULO_NUMERO', max_length=10)  # Field name made lowercase.
    modulo_letra = models.CharField(db_column='MODULO_LETRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modulo_piso = models.CharField(db_column='MODULO_PISO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modulo_puerta = models.CharField(db_column='MODULO_PUERTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modulo_localidad = models.CharField(db_column='MODULO_LOCALIDAD', max_length=100)  # Field name made lowercase.
    modulo_departamento = models.CharField(db_column='MODULO_DEPARTAMENTO', max_length=45)  # Field name made lowercase.
    modulo_region = models.CharField(db_column='MODULO_REGION', max_length=45)  # Field name made lowercase.
    modulo_sector = models.CharField(db_column='MODULO_SECTOR', max_length=45)  # Field name made lowercase.
    modulo_latitud = models.CharField(db_column='MODULO_LATITUD', max_length=25)  # Field name made lowercase.
    modulo_longitud = models.CharField(db_column='MODULO_LONGITUD', max_length=25)  # Field name made lowercase.
    modulo_punto_en_plano = models.IntegerField(db_column='MODULO_PUNTO_EN_PLANO')  # Field name made lowercase.
    modulo_cliente = models.CharField(db_column='MODULO_CLIENTE', max_length=100)  # Field name made lowercase.
    modulo_suministro = models.CharField(db_column='MODULO_SUMINISTRO', max_length=45)  # Field name made lowercase.
    modulo_cuenta = models.CharField(db_column='MODULO_CUENTA', max_length=45)  # Field name made lowercase.
    modulo_medidor_numero = models.CharField(db_column='MODULO_MEDIDOR_NUMERO', unique=True, max_length=45)  # Field name made lowercase.
    modulo_medidor_marca = models.CharField(db_column='MODULO_MEDIDOR_MARCA', max_length=45)  # Field name made lowercase.
    modulo_medidor_modelo = models.CharField(db_column='MODULO_MEDIDOR_MODELO', max_length=45)  # Field name made lowercase.
    modulo_medidor_diametro = models.CharField(db_column='MODULO_MEDIDOR_DIAMETRO', max_length=4)  # Field name made lowercase.
    modulo_ultima_lectura_fyh = models.DateTimeField(db_column='MODULO_ULTIMA_LECTURA_FYH', blank=True, null=True)  # Field name made lowercase.
    modulo_ultima_lectura_valor = models.IntegerField(db_column='MODULO_ULTIMA_LECTURA_VALOR', blank=True, null=True)  # Field name made lowercase.
    modulo_alarmas = models.CharField(db_column='MODULO_ALARMAS', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulo'


class Modulos(models.Model):
    id_modulos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    icono = models.CharField(max_length=50, blank=True, null=True)
    id_parent = models.PositiveIntegerField(blank=True, null=True)
    menu = models.CharField(max_length=1)
    jerarquia = models.PositiveIntegerField()
    is_sub = models.CharField(max_length=1)
    mostrar = models.CharField(max_length=1)
    mostrar_ose = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'modulos'


class Trasmisiones(models.Model):
    trasmisiones_id = models.AutoField(db_column='TRASMISIONES_ID', primary_key=True)  # Field name made lowercase.
    trasmisiones_gateway = models.IntegerField(db_column='TRASMISIONES_GATEWAY', blank=True, null=True)  # Field name made lowercase.
    trasmisiones_signal = models.CharField(db_column='TRASMISIONES_SIGNAL', max_length=5)  # Field name made lowercase.
    trasmisiones_fyh = models.DateTimeField(db_column='TRASMISIONES_FYH')  # Field name made lowercase.
    trasmisiones_nlecturas = models.IntegerField(db_column='TRASMISIONES_NLECTURAS')  # Field name made lowercase.
    trasmisiones_lecturas_mod0 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD0')  # Field name made lowercase.
    trasmisiones_lecturas_mod1 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD1')  # Field name made lowercase.
    trasmisiones_lecturas_mod2 = models.IntegerField(db_column='TRASMISIONES_LECTURAS_MOD2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trasmisiones'
