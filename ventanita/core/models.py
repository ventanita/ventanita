# Copyright 2015 by Pedro Palacios (Wesitos). All rights reserved.
# Revisions 2015 copyright by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.db import models


class Candidato(models.Model):
    candidato_jne_id = models.IntegerField(help_text='ID asignado por el JNE')

    # Datos Personales
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=300)
    apellido_materno = models.CharField(max_length=300)
    apellido_paterno = models.CharField(max_length=300)
    sexo = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    org_politica = models.CharField(max_length=300)

    # Familia
    madre = models.CharField(max_length=300)
    conyuge = models.CharField(max_length=300)
    padre = models.CharField(max_length=300)

    # Postulacion
    postulacion_cargo = models.CharField(max_length=300)
    postulacion_ubigeo = models.CharField(max_length=300)
    postulacion_distrito = models.CharField(max_length=300)
    postulacion_provincia = models.CharField(max_length=300)
    postulacion_departamento = models.CharField(max_length=300)
    postulacion_designacion = models.CharField(max_length=300)

    # Nacimiento
    nacimiento_pais = models.CharField(max_length=300)
    nacimiento_ubigeo = models.CharField(max_length=300)
    nacimiento_fecha = models.DateField(null=True, blank=True)
    nacimiento_distrito = models.CharField(max_length=300)
    nacimiento_provincia = models.CharField(max_length=300)
    nacimiento_departamento = models.CharField(max_length=300)

    # Residencia
    residencia_lugar = models.CharField(max_length=300, blank=True)
    residencia_ubigeo = models.CharField(max_length=300, blank=True)
    residencia_distrito = models.CharField(max_length=300, blank=True)
    residencia_tiempo = models.CharField(max_length=300, blank=True)
    residencia_provincia = models.CharField(max_length=300, blank=True)
    residencia_departamento = models.CharField(max_length=300, blank=True)

    # bienes_muebles = relationship("BienMueble", backref="candidato")
    # bienes_inmuebles = relationship("BienInmueble", backref="candidato")
    # otra_experiencia = relationship("OtraExperiencia", backref="candidato")
    # militancia = relationship("Militancia", backref="candidato")
    # civil = relationship("Civil", backref="candidato")

    # educacion_basica_primaria = relationship("Primaria", backref="candidato")
    # educacion_basica_secundaria = relationship("Secundaria", backref="candidato")
    # educacion_superior_postgrado = relationship("Postgrado", backref="candidato")
    # educacion_superior_universitario = relationship("Universitario", backref="candidato")
    # educacion_superior_tecnico = relationship("Tecnico", backref="candidato")
    # partidario = relationship("Partidario", backref="candidato")
    # eleccion = relationship("Eleccion", backref="candidato")
    # experiencia = relationship("Experiencia", backref="candidato")
    # observaciones = relationship("Observacion", backref="candidato")


class BienMueble(models.Model):
    bien = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    caracteristicas = models.CharField(max_length=300)
    valor = models.IntegerField()
    candidato = models.ForeignKey('Candidato')


class BienInmueble(models.Model):
    registro = models.CharField(max_length=300)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class OtraExperiencia(models.Model):
    cargo = models.CharField(max_length=300)
    entidad = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    candidato = models.ForeignKey('Candidato')


class Militancia(models.Model):
    inicio = models.IntegerField()
    fin = models.IntegerField()
    org_politica = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Civil(models.Model):
    """Antecedentes civiles"""
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Penal(models.Model):
    """Antecedentes penales"""
    delito = models.CharField(max_length=300)
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)
    fecha_sentencia = models.DateField()
    candidato = models.ForeignKey('Candidato')


class Postgrado(models.Model):
    concluido = models.NullBooleanField()
    grado_titulo = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    inst_educativa = models.CharField(max_length=300)
    especialidad = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Tecnico(models.Model):
    concluido = models.NullBooleanField()
    provincia = models.CharField(max_length=300)
    curso = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    especialidad = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    inst_educativa = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Universitario(models.Model):
    departamento = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    concluido = models.NullBooleanField()
    grado_titulo = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    facultad = models.CharField(max_length=300)
    carrera = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    inst_educativa = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Partidario(models.Model):
    cargo = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    org_politica = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    candidato = models.ForeignKey('Candidato')


class Eleccion(models.Model):
    proceso_electoral = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    distrito = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    org_politica = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Experiencia(models.Model):
    sector = models.CharField(max_length=300)
    cargo = models.IntegerField()
    provincia = models.CharField(max_length=300)
    empleador = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    departamento = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Colegio(models.Model):
    inst_educativa = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    estudiante = models.ManyToManyField(Candidato, through='Primaria')


class Primaria(models.Model):
    concluido = models.NullBooleanField()
    inicio = models.IntegerField()
    fin = models.IntegerField()
    tipo_educacion = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')
    colegio = models.ForeignKey('Colegio')


class Secundaria(models.Model):
    concluido = models.NullBooleanField()
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    inst_educativa = models.CharField(max_length=300)
    candidato = models.ForeignKey('Candidato')


class Observacion(models.Model):
    referencia = models.CharField(max_length=300)
    anotacion = models.CharField(max_length=2000)
    candidato = models.ForeignKey('Candidato')


# Registro de morosos por alimentos. REDAM.

class DeudorRedam(models.Model):
    """Demandado"""
    dni = models.CharField(max_length=8)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombres = models.CharField(max_length=200)
    url = models.URLField()
    debe = models.FloatField()


class DeudorRedamVinculo(models.Model):
    """Demandante"""
    deudor = models.ForeignKey('DeudorRedam')
    vinculo = models.CharField(max_length=100)
    nombre_completo = models.CharField(max_length=300)
