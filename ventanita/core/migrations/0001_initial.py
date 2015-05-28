# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BienInmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('registro', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
                ('tipo', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='BienMueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('bien', models.CharField(max_length=300)),
                ('tipo', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('caracteristicas', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('candidato_jne_id', models.IntegerField(help_text='ID asignado por el JNE')),
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=300)),
                ('apellido_materno', models.CharField(max_length=300)),
                ('apellido_paterno', models.CharField(max_length=300)),
                ('sexo', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('madre', models.CharField(max_length=300)),
                ('conyuge', models.CharField(max_length=300)),
                ('padre', models.CharField(max_length=300)),
                ('postulacion_cargo', models.CharField(max_length=300)),
                ('postulacion_ubigeo', models.CharField(max_length=300)),
                ('postulacion_distrito', models.CharField(max_length=300)),
                ('postulacion_provincia', models.CharField(max_length=300)),
                ('postulacion_departamento', models.CharField(max_length=300)),
                ('postulacion_designacion', models.CharField(max_length=300)),
                ('nacimiento_pais', models.CharField(max_length=300)),
                ('nacimiento_ubigeo', models.CharField(max_length=300)),
                ('nacimiento_fecha', models.DateField(null=True, blank=True)),
                ('nacimiento_distrito', models.CharField(max_length=300)),
                ('nacimiento_provincia', models.CharField(max_length=300)),
                ('nacimiento_departamento', models.CharField(max_length=300)),
                ('residencia_lugar', models.CharField(max_length=300, blank=True)),
                ('residencia_ubigeo', models.CharField(max_length=300, blank=True)),
                ('residencia_distrito', models.CharField(max_length=300, blank=True)),
                ('residencia_tiempo', models.CharField(max_length=300, blank=True)),
                ('residencia_provincia', models.CharField(max_length=300, blank=True)),
                ('residencia_departamento', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('materia', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='DeudorRedam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('dni', models.CharField(max_length=8)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('debe', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DeudorRedamVinculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('vinculo', models.CharField(max_length=100)),
                ('nombre_completo', models.CharField(max_length=300)),
                ('deudor', models.ForeignKey(to='core.DeudorRedam')),
            ],
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('proceso_electoral', models.CharField(max_length=300)),
                ('cargo', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('distrito', models.CharField(max_length=300)),
                ('ambito', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tipo_de_estudio', models.CharField(max_length=300, choices=[('primaria', 'primaria'), ('tecnica', 'tecnica'), ('secundaria', 'secundaria'), ('universitaria', 'universitaria'), ('postgrado', 'postgrado')], blank=True, help_text='Colegio, instituto, universidad y grado de instrucción.')),
                ('concluido', models.NullBooleanField()),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('curso', models.CharField(max_length=300)),
                ('especialidad', models.CharField(max_length=300)),
                ('grado_titulo', models.CharField(max_length=300)),
                ('facultad', models.CharField(max_length=300)),
                ('carrera', models.CharField(max_length=300)),
                ('tipo', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sector', models.CharField(max_length=300)),
                ('cargo', models.IntegerField()),
                ('provincia', models.CharField(max_length=300)),
                ('empleador', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('departamento', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='InstitucionEducativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
                ('pais', models.CharField(max_length=300)),
                ('extranjero', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Militancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('org_politica', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('referencia', models.CharField(max_length=300)),
                ('anotacion', models.CharField(max_length=2000)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='OtraExperiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cargo', models.CharField(max_length=300)),
                ('entidad', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Partidario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cargo', models.CharField(max_length=300)),
                ('ambito', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Penal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('delito', models.CharField(max_length=300)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('fecha_sentencia', models.DateField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
        ),
        migrations.AddField(
            model_name='estudio',
            name='institucion_educativa',
            field=models.ForeignKey(to='core.InstitucionEducativa'),
        ),
        migrations.AddField(
            model_name='bienmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
        ),
        migrations.AddField(
            model_name='bieninmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
        ),
    ]
