# Copyright 2015 by Vitoko. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import _mssql
import csv


def replace(content):
    if content != '':
        return content.replace("'", "")


def importar(row, index):
    conn = _mssql.connect(server='s10.winhost.com:1433',
                          user='DB_76507_ventanita_user',
                          password='123abc$',
                          database='DB_76507_ventanita')
    query = "INSERT INTO Candidatos VALUES({21}, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', {20})".format(
        replace(row['ORGANIZACION POLITICA']),
        replace(row['CARGO AL QUE POSTULA']),
        replace(row['DEPARTAMENTO AL QUE POSTULA']),
        replace(row['PROVINCIA AL QUE POSTULA']),
        replace(row['DISTRITO AL QUE POSTULA']),
        replace(row['DESIGNACION']),
        replace(row['APELLIDO PATERNO']),
        replace(row['APELLIDO MATERNO']),
        replace(row['NOMBRE COMPLETO']),
        replace(row['SEXO']),
        replace(row['DNI']),
        replace(row['CORREO ELECTRONICO']),
        replace(row['DEPARTAMENTO DE NACIMIENTO']),
        replace(row['PROVINCIA DE NACIMIENTO']),
        replace(row['DISTRITO DE NACIMIENTO']),
        replace(row['FECHA DE NACIMIENTO']),
        replace(row['DEPARTAMENTO DE RESIDENCIA']),
        replace(row['PROVINCIA DE RESIDENCIA']),
        replace(row['DISTRITO DE RESIDENCIA']),
        replace(row['LUGAR DE RESIDENCIA']),
        replace(row['TIEMPO DE RESIDENCIA']),
        index)
    conn.execute_non_query(query)
    conn.close()


with open('../../dummy_data/dummy_data0.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    index = 1
    for row in reader:
        importar(row, index)
        index += 1
