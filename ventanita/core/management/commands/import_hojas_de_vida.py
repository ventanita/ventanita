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
        make_option('--hoja',
                    dest='hoja',
                    help='Enter name of Excel sheet number to import.'
                    ),
    )

    def handle(self, *args, **options):
        if options['tsvfile'] is None or options['hoja'] is None:
            error_msg = 'Enter name of tsv file as argument.' \
                        ' "python manage.py import_hojas_de_vida --tsvfile=hoja0.tsv --hoja=0 --settings=ventanita.settings.local'
            raise CommandError(error_msg)

        tsv_file = options['tsvfile']
        hoja = options['hoja']

        with codecs.open(tsv_file, "r") as file_handle:
            dump = file_handle.readlines()

        items = []
        n = len(dump)
        bar = pyprind.ProgBar(n)
        for line in dump:
            item = None

            if hoja == '0':
                item = self.parse_line(line)

            if item is not None:
                items.append(Candidato(**item))
            bar.update()
        Candidato.objects.bulk_create(items)

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
