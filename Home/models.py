# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id_admin = models.FloatField(primary_key=True)
    rut = models.CharField(max_length=12)
    pr_nombre = models.CharField(max_length=30)
    seg_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    fec_nac = models.DateField()
    sucursal_id_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='sucursal_id_sucursal')

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bodega(models.Model):
    id_bodega = models.IntegerField(primary_key=True)
    stock = models.IntegerField()
    direccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    sucursal_id_sucursal = models.OneToOneField('Sucursal', models.DO_NOTHING, db_column='sucursal_id_sucursal')

    class Meta:
        managed = False
        db_table = 'bodega'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)
    pass_field = models.CharField(db_column='pass', max_length=100)  # Field renamed because it was a Python reserved word.
    pr_nombre = models.CharField(max_length=30)
    seg_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    fec_nac = models.DateField()
    celular = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    total_productos = models.IntegerField()
    total_pago = models.IntegerField()
    libro_id_libro = models.ForeignKey('Libro', models.DO_NOTHING, db_column='libro_id_libro')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')

    class Meta:
        managed = False
        db_table = 'compra'


class ConfirmacionCompra(models.Model):
    pago_id_pago = models.OneToOneField('Pago', models.DO_NOTHING, db_column='pago_id_pago', primary_key=True)  # The composite primary key (pago_id_pago, compra_id_compra) found, that is not supported. The first column is selected.
    compra_id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='compra_id_compra')

    class Meta:
        managed = False
        db_table = 'confirmacion_compra'
        unique_together = (('pago_id_pago', 'compra_id_compra'),)


class ConfirmacionPago(models.Model):
    despacho_id_despacho = models.OneToOneField('Despacho', models.DO_NOTHING, db_column='despacho_id_despacho', primary_key=True)  # The composite primary key (despacho_id_despacho, pago_id_pago) found, that is not supported. The first column is selected.
    pago_id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='pago_id_pago')

    class Meta:
        managed = False
        db_table = 'confirmacion_pago'
        unique_together = (('despacho_id_despacho', 'pago_id_pago'),)


class Despacho(models.Model):
    id_despacho = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'despacho'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Encargado(models.Model):
    id_encargado = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    pr_nombre = models.CharField(max_length=30)
    seg_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    fec_nac = models.DateField()
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        managed = False
        db_table = 'encargado'


class EstadoDespacho(models.Model):
    id_est_despacho = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_despacho'


class Libro(models.Model):
    id_libro = models.IntegerField(primary_key=True)
    nombre_libro = models.CharField(max_length=50)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        managed = False
        db_table = 'libro'


class Mantencion(models.Model):
    id_mantencion = models.IntegerField(primary_key=True)
    fec_mantencion = models.DateField()

    class Meta:
        managed = False
        db_table = 'mantencion'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fec_transaccion = models.DateField()

    class Meta:
        managed = False
        db_table = 'pago'


class Repartidor(models.Model):
    id_repartidor = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    pr_nombre = models.CharField(max_length=30)
    seg_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    fec_nac = models.DateField()

    class Meta:
        managed = False
        db_table = 'repartidor'


class Seguimiento(models.Model):
    estado_despacho_id_est_des = models.OneToOneField(EstadoDespacho, models.DO_NOTHING, db_column='estado_despacho_id_est_des', primary_key=True)  # The composite primary key (estado_despacho_id_est_des, despacho_id_despacho) found, that is not supported. The first column is selected.
    despacho_id_despacho = models.ForeignKey(Despacho, models.DO_NOTHING, db_column='despacho_id_despacho')

    class Meta:
        managed = False
        db_table = 'seguimiento'
        unique_together = (('estado_despacho_id_est_des', 'despacho_id_despacho'),)


class SolicitudDespacho(models.Model):
    repartidor_id_repartidor = models.OneToOneField(Repartidor, models.DO_NOTHING, db_column='repartidor_id_repartidor', primary_key=True)  # The composite primary key (repartidor_id_repartidor, despacho_id_despacho) found, that is not supported. The first column is selected.
    despacho_id_despacho = models.ForeignKey(Despacho, models.DO_NOTHING, db_column='despacho_id_despacho')

    class Meta:
        managed = False
        db_table = 'solicitud_despacho'
        unique_together = (('repartidor_id_repartidor', 'despacho_id_despacho'),)


class SolicitudMantencion(models.Model):
    libro_id_libro = models.OneToOneField(Libro, models.DO_NOTHING, db_column='libro_id_libro', primary_key=True)  # The composite primary key (libro_id_libro, mantencion_id_mantencion) found, that is not supported. The first column is selected.
    mantencion_id_mantencion = models.ForeignKey(Mantencion, models.DO_NOTHING, db_column='mantencion_id_mantencion')

    class Meta:
        managed = False
        db_table = 'solicitud_mantencion'
        unique_together = (('libro_id_libro', 'mantencion_id_mantencion'),)


class SolicitudTecnico(models.Model):
    mantencion_id_mantencion = models.OneToOneField(Mantencion, models.DO_NOTHING, db_column='mantencion_id_mantencion', primary_key=True)  # The composite primary key (mantencion_id_mantencion, tecnico_id_tecnico) found, that is not supported. The first column is selected.
    tecnico_id_tecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='tecnico_id_tecnico')

    class Meta:
        managed = False
        db_table = 'solicitud_tecnico'
        unique_together = (('mantencion_id_mantencion', 'tecnico_id_tecnico'),)


class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tecnico(models.Model):
    id_tecnico = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=12)
    pr_nombre = models.CharField(max_length=30)
    seg_nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    fec_nac = models.DateField()

    class Meta:
        managed = False
        db_table = 'tecnico'
