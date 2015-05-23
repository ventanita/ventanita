# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/demo/')
