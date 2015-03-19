#!/usr/bin/env python

# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ventanita.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
