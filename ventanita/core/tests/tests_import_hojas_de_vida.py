# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import os

from django.core.management import call_command
from django.core.management import CommandError
from django.conf import settings
from django.test import TestCase

from core.models import Candidato


class TestCommandImportHojasDeVida(TestCase):
    def setUp(self):
        dummy_data = os.path.join(settings.BASE_DIR, '..', '..', 'dummy_data', 'dummy_data0.tsv')
        args = []
        opts = {'tsvfile': dummy_data, 'sheet': '0'}
        cmd = 'import_hojas_de_vida'
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
