# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import codecs
import datetime
from optparse import make_option

import pyprind
from django.core.management.base import BaseCommand, CommandError

from core.models import Candidato


class Command(BaseCommand):
    """
    Imports TSV data from 'Hojas de vida'
    """
    option_list = BaseCommand.option_list + (
        make_option('--tsvfile',
                    dest='tsvfile',
                    help='Enter name of tsv file as argument.'
                    ),
        make_option('--sheet',
                    dest='sheet',
                    help='Enter name of Excel sheet number to import.'
                    ),
    )

    def handle(self, *args, **options):
        if options['tsvfile'] is None or options['sheet'] is None:
            error_msg = 'Enter name of tsv file as argument.' \
                        ' "python manage.py import_hojas_de_vida --tsvfile=hoja0.tsv --sheet=0 --settings=ventanita.settings.local'
            raise CommandError(error_msg)

        tsv_file = options['tsvfile']
        sheet = options['sheet']

        with codecs.open(tsv_file, "r") as file_handle:
            dump = file_handle.readlines()

        items = []
        n = len(dump)
        bar = pyprind.ProgBar(n)

        candidatos_objects = Candidato.objects.all()
        candidatos_dict = self.as_dict(candidatos_objects)

        if sheet == '0':
            for line in dump:
                item = self.parse_line(line)
                if item is not None:
                    items.append(Candidato(**item))
                bar.update()
        elif sheet == '1':
            self.import_colegios(dump)
            # item = self.parse_line_sheet1(line, candidatos_dict)

        Candidato.objects.bulk_create(items)

    def import_colegios(self, dump):
        colegios = set()
        for line in dump:
            line = line.strip()
            # line = line.replace('\t\t', '\t')
            fields = line.split('\t')
            # if fields[1] == 'DNI':
                # continue
            # Primaria
            colegio = dict()
            colegio['inst_educativa'] = fields[5]
            colegio['departamento'] = fields[12]
            colegio['provincia'] = fields[13]
            colegio['distrito'] = fields[14]
            try:
                colegio['extranjero'] = fields[18]
            except IndexError:
                colegio['extranjero'] = ''

            try:
                colegio['pais'] = fields[19]
            except IndexError:
                colegio['pais'] = ''
            print(colegio)

            # Secundaria
            colegio = dict()
            colegio['inst_educativa'] = fields[6]

    def parse_line(self, line):
        line = line.strip()
        if line != '':
            fields = line.split('\t')
            item = dict()
            item['dni'] = fields[0]
            item['postulacion_departamento'] = fields[1]
            item['postulacion_provincia'] = fields[2]
            item['postulacion_distrito'] = fields[3]
            item['candidato_jne_id'] = fields[4]
            item['org_politica'] = fields[5]
            item['postulacion_cargo'] = fields[6]
            item['postulacion_designacion'] = fields[7]
            item['apellido_paterno'] = fields[8]
            item['apellido_materno'] = fields[9]
            item['nombres'] = fields[10]
            item['sexo'] = fields[11]
            item['email'] = fields[12]
            item['nacimiento_departamento'] = fields[13]
            item['nacimiento_provincia'] = fields[14]
            item['nacimiento_distrito'] = fields[15]
            try:
                item['nacimiento_fecha'] = datetime.datetime.strptime(fields[16], '%Y-%m-%d')
            except ValueError:
                # TODO ignore this field for now as data is mangled from Excel
                item['nacimiento_fecha'] = None

            try:
                item['residencia_departamento'] = fields[17]
            except IndexError:
                item['residencia_departamento'] = ''

            try:
                item['residencia_provincia'] = fields[18]
            except IndexError:
                item['residencia_provincia'] = ''

            try:
                item['residencia_distrito'] = fields[19]
            except IndexError:
                item['residencia_distrito'] = ''

            try:
                item['residencia_lugar'] = fields[20]
            except IndexError:
                item['residencia_lugar'] = ''

            try:
                item['residencia_tiempo'] = fields[21]
            except IndexError:
                item['residencia_tiempo'] = ''

            if item['dni'] != 'DNI':
                return item
        return None

    def parse_line_sheet1(self, line, candidatos):
        line = line.strip()
        if line != '':
            fields = line.split('\t')
            item = dict()
            dni = fields[1]

            if dni == 'DNI':
                return None

            print(">>>>>>>dni", dni)
            print(candidatos[dni].dni)


            if item['dni'] != 'DNI':
                return item
        return None

    def as_dict(self, candidatos_objects):
        mydict = dict()
        for i in candidatos_objects:
            mydict[i.dni] = i
        return mydict
