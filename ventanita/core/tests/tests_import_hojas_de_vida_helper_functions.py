# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.test import TestCase

from core.management.commands.import_hojas_de_vida import get_institucion_superior
from core.management.commands.import_hojas_de_vida import get_superior_rango


class TestCommandImportHojasDeVida(TestCase):
    def test_get_institution_superior(self):
        with open('dummy_data/dummy_data2.tsv', 'r') as handle:
            line = handle.readlines()[1]
        fields = line.split('\t')
        result = get_institucion_superior(fields)
        expected = 'NO'
        self.assertEqual(expected, result['extranjero'])

    def test_get_institution_superior_range(self):
        with open('dummy_data/dummy_data2.tsv', 'r') as handle:
            line = handle.readlines()[1]
        fields = line.split('\t')
        result = get_superior_rango(fields)
        expected = ('1990', '1996')
        self.assertEqual(expected, result)
