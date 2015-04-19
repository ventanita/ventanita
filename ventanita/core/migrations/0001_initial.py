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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('registro', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
                ('tipo', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BienMueble',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('bien', models.CharField(max_length=300)),
                ('tipo', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('caracteristicas', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('nacimiento_fecha', models.DateField(blank=True, null=True)),
                ('nacimiento_distrito', models.CharField(max_length=300)),
                ('nacimiento_provincia', models.CharField(max_length=300)),
                ('nacimiento_departamento', models.CharField(max_length=300)),
                ('residencia_lugar', models.CharField(blank=True, max_length=300)),
                ('residencia_ubigeo', models.CharField(blank=True, max_length=300)),
                ('residencia_distrito', models.CharField(blank=True, max_length=300)),
                ('residencia_tiempo', models.CharField(blank=True, max_length=300)),
                ('residencia_provincia', models.CharField(blank=True, max_length=300)),
                ('residencia_departamento', models.CharField(blank=True, max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('materia', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('inst_educativa', models.CharField(max_length=300)),
                ('pais', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeudorRedam',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('dni', models.CharField(max_length=8)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('debe', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeudorRedamVinculo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('vinculo', models.CharField(max_length=100)),
                ('nombre_completo', models.CharField(max_length=300)),
                ('deudor', models.ForeignKey(to='core.DeudorRedam')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Militancia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('org_politica', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('referencia', models.CharField(max_length=300)),
                ('anotacion', models.CharField(max_length=2000)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtraExperiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cargo', models.CharField(max_length=300)),
                ('entidad', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partidario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cargo', models.CharField(max_length=300)),
                ('ambito', models.CharField(max_length=300)),
                ('org_politica', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Penal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('delito', models.CharField(max_length=300)),
                ('expediente', models.CharField(max_length=300)),
                ('juzgado', models.CharField(max_length=300)),
                ('fallo', models.CharField(max_length=300)),
                ('fecha_sentencia', models.DateField()),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgrado',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('concluido', models.NullBooleanField()),
                ('grado_titulo', models.CharField(max_length=300)),
                ('tipo', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('pais', models.CharField(max_length=300)),
                ('inst_educativa', models.CharField(max_length=300)),
                ('especialidad', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Primaria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('concluido', models.NullBooleanField()),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('tipo_educacion', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
                ('colegio', models.ForeignKey(to='core.Colegio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Secundaria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('concluido', models.NullBooleanField()),
                ('provincia', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('pais', models.CharField(max_length=300)),
                ('inst_educativa', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('concluido', models.NullBooleanField()),
                ('provincia', models.CharField(max_length=300)),
                ('curso', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
                ('especialidad', models.CharField(max_length=300)),
                ('departamento', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('pais', models.CharField(max_length=300)),
                ('inst_educativa', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Universitario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('departamento', models.CharField(max_length=300)),
                ('pais', models.CharField(max_length=300)),
                ('concluido', models.NullBooleanField()),
                ('grado_titulo', models.CharField(max_length=300)),
                ('provincia', models.CharField(max_length=300)),
                ('facultad', models.CharField(max_length=300)),
                ('carrera', models.CharField(max_length=300)),
                ('inicio', models.IntegerField()),
                ('fin', models.IntegerField()),
                ('inst_educativa', models.CharField(max_length=300)),
                ('distrito', models.CharField(max_length=300)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='colegio',
            name='estudiante',
            field=models.ManyToManyField(through='core.Primaria', to='core.Candidato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bienmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bieninmueble',
            name='candidato',
            field=models.ForeignKey(to='core.Candidato'),
            preserve_default=True,
        ),
    ]
