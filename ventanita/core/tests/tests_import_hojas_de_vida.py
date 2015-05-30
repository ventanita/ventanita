# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import datetime
import os

from django.core.management import call_command
from django.core.management import CommandError
from django.conf import settings
from django.test import TestCase

from core.models import Candidato
from core.models import Estudio
from core.models import InstitucionEducativa


class TestCommandImportHojasDeVida(TestCase):
    def setUp(self):
        dummy_data = os.path.join(settings.BASE_DIR, '..', '..', 'dummy_data', 'dummy_data0.tsv')
        args = []
        opts = {'tsvfile': dummy_data, 'sheet': '0'}
        cmd = 'import_hojas_de_vida'
        call_command(cmd, *args, **opts)

        dummy_data = os.path.join(settings.BASE_DIR, '..', '..', 'dummy_data', 'dummy_data1.tsv')
        opts = {'tsvfile': dummy_data, 'sheet': '1'}
        call_command(cmd, *args, **opts)

    def test_import_fail(self):
        args = []
        opts = {}
        cmd = 'import_hojas_de_vida'
        self.assertRaises(CommandError, call_command, cmd, *args, **opts)

    def test_import(self):
        c = Candidato.objects.get(dni='00020789')
        result = c.nombres
        expected = 'ANGELA EDITH'
        self.assertEqual(expected, result)

    def test_import_date_of_birth(self):
        c = Candidato.objects.get(dni='00020789')
        result = c.nacimiento_fecha
        expected = datetime.date(1952, 1, 4)
        self.assertEqual(expected, result)

    def test_import_education_for_candidate_primaria(self):
        c = Candidato.objects.get(dni='23202638')
        result = Estudio.objects.get(candidato=c, tipo_de_estudio='primaria')
        expected = 'I. E SAN MIGUEL'
        self.assertEqual(expected, result.institucion_educativa.nombre)

    def test_import_education_for_candidate_secundaria(self):
        c = Candidato.objects.get(dni='43543320')
        result = Estudio.objects.get(candidato=c, tipo_de_estudio='secundaria')
        expected = 'I.E. SECUNDARIO VIRGILIO ESPINOZA VAEZ'
        self.assertEqual(expected, result.institucion_educativa.nombre)

    def test_import_institucion_educativa(self):
        result = InstitucionEducativa.objects.all().values('nombre', 'departamento', 'provincia',
                                                           'distrito', 'extranjero', 'pais')
        expected = {'nombre': 'ESCUELA PRIMARIA DE VARONES MIGUEL GRAU - SAUSAL',
                    'departamento': 'LA LIBERTAD', 'provincia': 'ASCOPE', 'distrito': 'CHICAMA',
                    'extranjero': '', 'pais': ''}
        self.assertTrue(expected in result)
