# Copyright 2015 by Pedro Palacios (Wesitos). All rights reserved.
# Revisions 2015 copyright by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.db import models


class Candidato(models.Model):
    # Datos Personales
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=300)
    apellido_materno = models.CharField(max_length=300)
    apellido_paterno = models.CharField(max_length=300)
    sexo = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

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
    nacimiento_fecha = models.DateField()
    nacimiento_distrito = models.CharField(max_length=300)
    nacimiento_provincia = models.CharField(max_length=300)
    nacimiento_departamento = models.CharField(max_length=300)

    # Residencia
    residencia_lugar = models.CharField(max_length=300)
    residencia_ubigeo = models.CharField(max_length=300)
    residencia_distrito = models.CharField(max_length=300)
    residencia_tiempo = models.CharField(max_length=300)
    residencia_provincia = models.CharField(max_length=300)
    residencia_departamento = models.CharField(max_length=300)

    bienes_muebles = relationship("BienMueble", backref="candidato")
    bienes_inmuebles = relationship("BienInmueble", backref="candidato")
    otra_experiencia = relationship("OtraExperiencia", backref="candidato")
    militancia = relationship("Militancia", backref="candidato")
    civil = relationship("Civil", backref="candidato")
    educacion_basica_primaria = relationship("Primaria", backref="candidato")
    educacion_basica_secundaria = relationship("Secundaria", backref="candidato")
    educacion_superior_postgrado = relationship("Postgrado", backref="candidato")
    educacion_superior_universitario = relationship("Universitario", backref="candidato")
    educacion_superior_tecnico = relationship("Tecnico", backref="candidato")
    partidario = relationship("Partidario", backref="candidato")
    eleccion = relationship("Eleccion", backref="candidato")
    experiencia = relationship("Experiencia", backref="candidato")
    observaciones = relationship("Observacion", backref="candidato")


class BienMueble(models.Model):
    __tablename__ = 'bienes_muebles'
    id = Column(Integer, primary_key=True)
    bien = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    caracteristicas = models.CharField(max_length=300)
    valor = models.IntegerField()

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class BienInmueble(models.Model):
    __tablename__ = 'bienes_inmuebles'
    id = Column(Integer, primary_key=True)
    registro = models.CharField(max_length=300)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class OtraExperiencia(models.Model):
    __tablename__ = 'otra_experiencia'
    id = Column(Integer, primary_key=True)
    cargo = models.CharField(max_length=300)
    entidad = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Militancia(models.Model):
    __tablename__ = 'militancias'
    id = Column(Integer, primary_key=True)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    orgPolitica = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Civil(models.Model):
    """Antecedentes civiles"""
    __tablename__ = 'civiles'
    id = Column(Integer, primary_key=True)
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Penal(models.Model):
    """Antecedentes penales"""
    __tablename__ = 'penales'
    id = Column(Integer, primary_key=True)
    delito = models.CharField(max_length=300)
    expediente = models.CharField(max_length=300)
    juzgado = models.CharField(max_length=300)
    fallo = models.CharField(max_length=300)
    fechaSentencia = models.DateField()

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Postgrado(models.Model):
    __tablename__ = 'educacion_superior_postgrado'
    id = Column(Integer, primary_key=True)
    concluido = models.BooleanField()
    gradoTitulo = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    instEducativa = models.CharField(max_length=300)
    especialidad = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Tecnico(models.Model):
    __tablename__ = 'educacion_superior_tecnico'
    id = Column(Integer, primary_key=True)
    concluido = models.BooleanField()
    provincia = models.CharField(max_length=300)
    curso = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    especialidad = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    instEducativa = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Universitario(models.Model):
    __tablename__ = 'educacion_superior_universitario'
    id = Column(Integer, primary_key=True)
    departamento = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    concluido = models.BooleanField()
    gradoTitulo = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    facultad = models.CharField(max_length=300)
    carrera = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    instEducativa = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Partidario(models.Model):
    __tablename__ = 'partidario'
    id = Column(Integer, primary_key=True)
    cargo = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    orgPolitica = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Eleccion(models.Model):
    __tablename__ = 'eleccion'
    id = Column(Integer, primary_key=True)
    procesoElectoral = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    distrito = models.CharField(max_length=300)
    ambito = models.CharField(max_length=300)
    orgPolitica = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Experiencia(models.Model):
    __tablename__ = 'experiencia'
    id = Column(Integer, primary_key=True)
    sector = models.CharField(max_length=300)
    cargo = models.IntegerField()
    provincia = models.CharField(max_length=300)
    empleador = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    departamento = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Secundaria(models.Model):
    __tablename__ = 'educacion_basica_secundaria'
    id = Column(Integer, primary_key=True)
    concluido = models.BooleanField()
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()
    pais = models.CharField(max_length=300)
    instEducativa = models.CharField(max_length=300)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Primaria(models.Model):
    __tablename__ = 'educacion_basica_primaria'
    id = Column(Integer, primary_key=True)
    concluido = models.BooleanField()
    provincia = models.CharField(max_length=300)
    departamento = models.CharField(max_length=300)
    distrito = models.CharField(max_length=300)
    pais = models.CharField(max_length=300)
    instEducativa = models.CharField(max_length=300)
    inicio = models.IntegerField()
    fin = models.IntegerField()

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))


class Observacion(models.Model):
    __tablename__ = 'observaciones'
    id = Column(Integer, primary_key=True)
    referencia = models.CharField(max_length=300)
    anotacion = models.CharField(max_length=2000)

    id_candidato = Column(Integer, ForeignKey('candidatos.id'))
