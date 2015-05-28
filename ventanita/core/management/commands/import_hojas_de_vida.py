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
from core.models import InstitucionEducativa
from core.utils import get_item_from_list


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
            error_msg = 'Enter name of tsv file and sheet number as argument.' \
                        ' "python manage.py import_hojas_de_vida --tsvfile=hoja0.tsv --sheet=0 --settings=ventanita.settings.local'
            raise CommandError(error_msg)

        tsv_file = options['tsvfile']
        sheet = options['sheet']

        with codecs.open(tsv_file, "r") as file_handle:
            dump = file_handle.readlines()

        if sheet == '0':
            items = []
            n = len(dump)
            bar = pyprind.ProgBar(n)
            for line in dump:
                item = self.parse_line(line)
                if item is not None:
                    items.append(Candidato(**item))
                bar.update()
            Candidato.objects.bulk_create(items)
        elif sheet == '1':
            self.import_institucion_educativa(dump)

    def import_institucion_educativa(self, dump):
        instituciones = []

        n = len(dump)
        bar = pyprind.ProgBar(n)
        for line in dump:
            fields = line.strip().split('\t')

            this_inst_edu = get_institucion_primaria(fields)
            if this_inst_edu not in instituciones:
                instituciones.append(this_inst_edu)

            this_inst_edu = get_institucion_secundaria(fields)
            if this_inst_edu not in instituciones:
                instituciones.append(this_inst_edu)
            bar.update()

        upload_instituciones(instituciones)

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


def get_institucion_primaria(fields):
    nombre_primaria = get_item_from_list(fields, 5)
    departamento_primaria = get_item_from_list(fields, 12)
    provincia_primaria = get_item_from_list(fields, 13)
    distrito_primaria = get_item_from_list(fields, 14)
    extranjero = get_item_from_list(fields, 20)
    pais = get_item_from_list(fields, 21)
    this_inst_edu = {
        'nombre': nombre_primaria,
        'departamento': departamento_primaria,
        'provincia': provincia_primaria,
        'distrito': distrito_primaria,
        'extranjero': extranjero,
        'pais': pais,
    }
    return this_inst_edu


def get_institucion_secundaria(fields):
    nombre_secundaria = get_item_from_list(fields, 6)
    departamento_secundaria = get_item_from_list(fields, 17)
    provincia_secundaria = get_item_from_list(fields, 18)
    distrito_secundaria = get_item_from_list(fields, 19)
    extranjero = get_item_from_list(fields, 20)
    pais = get_item_from_list(fields, 21)
    this_inst_edu = {
        'nombre': nombre_secundaria,
        'departamento': departamento_secundaria,
        'provincia': provincia_secundaria,
        'distrito': distrito_secundaria,
        'extranjero': extranjero,
        'pais': pais,
    }
    return this_inst_edu


def upload_instituciones(instituciones):
    objs = []
    for i in instituciones:
        this_inst = InstitucionEducativa(**i)
        objs.append(this_inst)
    InstitucionEducativa.objects.bulk_create(objs)
