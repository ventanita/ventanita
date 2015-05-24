[![Build Status](https://travis-ci.org/ventanita/ventanita.svg?branch=master)](https://travis-ci.org/ventanita/ventanita)
[![Coverage Status](https://coveralls.io/repos/ventanita/ventanita/badge.svg)](https://coveralls.io/r/ventanita/ventanita)
[![Stories in Progress](https://badge.waffle.io/ventanita/ventanita.png?label=in progress&title=In Progress)](https://waffle.io/ventanita/ventanita)

[![Throughput Graph](https://graphs.waffle.io/ventanita/ventanita/throughput.svg)](https://waffle.io/ventanita/ventanita/metrics)

#Esta es ventanita

[![Join the chat at https://gitter.im/ventanita/ventanita](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ventanita/ventanita?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Poyecto de periodismo de datos con miras a las elecciones presidenciales,
congresales 2016.

Ventanita is un proyecto desarrollado por voluntarios. Tus contribuciones y mejoras
al código son bienvenidas.

## Contenido
* [Antecedentes](#antecedentes).
* [Objetivo principal](#objetivo-principal).
* [Cómo instalar Ventanita?](#cómo-instalar-ventanita)
* [Configurar Ventanita](#configurar-ventanita).
* [Ejecutar la aplicación](#ejecutar-la-aplicación).
* [Scripts para importar datos](#scripts-para-importar-datos).
* [Licencia](#licencia).

## Antecedentes
En las pasada campaña de Elecciones Regionales y Municipales 2014 ejecutamos el
proyecto **Verita** <http://utero.pe/tag/verita/>.

* Vale la pena hacer algo similar?
* Algo mejor?

Necesitamos ideas. Aporte y discusión de ideas aquí:
<https://github.com/aniversarioperu/ventanita/issues>

## Objetivo principal
Hacer un *aplicativo* web usando el **framework Django**. Este aplicativo permitirá 
que usuarios puedan dar evaluar rápidamente la idoneidad de los candidatos y
partidos políticos que se presenten a las Elecciones 2016.

Idealmente algo parecido al aplicativo uterino <http://www.selallevanfacil.info/home/>.


## Cómo instalar Ventanita?
Sigue estos pasos para instalar Ventanita en tu computadora y así poder modificar, corregir y agregar
funciones y herramientas al software. Estas instrucciones asumen que tienes una computadora con 
Ubuntu Linux.

### Instalar Ventanita
Es necesario que hagas un **fork** a este repositorio para tenerlo en tu cuenta de Github. Luego 
puedes clonar el respositorio en tu computadora (para eso debes tener instalado el software **git**).

```shell
sudo apt-get install git
```

Usa el siguiente comando para clonar el repo en tu computadora (reemplaza **aniversarioperu** con
tu username en Github:

```shell
git clone https://github.com/aniversarioperu/ventanita.git
```

Es buena idea crear un **virtual environment** para que sea tu área de trabajo. Ver más info sobre
la instalación de [virtualenvwrapper aquí](https://virtualenvwrapper.readthedocs.org/en/latest/).

```shell
mkvirtualenv -p /usr/bin/python3 ventanita
workon ventanita
```

Ventanita depende de varias "librerías" en Python. Para instalarlas en tu **virtual environment**:
```shell
cd ventanita
pip install -r requirements/testing.txt
```

### Instalar PostgreSQL
Ventanita almacena todos sus datos en una base de datos PostgreSQL. 
[Aquí está un excelente tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)
para la instalación de este software.

## Configurar Ventanita
Puedes poner tus datos de desarrollo local en un archivo ``config.json``,
asegurándote que haya sido incluido en tu ``.gitignore``.

```javascript
{
    "SECRET_KEY": "crear una clave secreta",
    "DB_USER": "usuario de base de datos postgreSQL",
    "DB_PASS": "tu contraseña para la base de datos",
    "DB_NAME": "ventanita",
    "DB_PORT": "5432",
    "DB_HOST": "localhost"
}
```

## Ejecutar la aplicación
Puede usar el ``Makefile`` de ventanita:

```shell
make migrations
make serve
```

Podrás ver la Ventanita en todo su esplendor apuntado tu navegador web a esta dirección:
``http://localhost:8000``

## Scripts para importar datos
Van en el folder ``scripts_for_imports``:

* Puedes importar el ``dummy_data`` a una base de datos MSSQL usando el script
  ``import_to_mssql.py``.
* Importar registros del REDAM: 
  ``python ventanita/manage.py import_redam --jsonfile=redam.jl --settings=ventanita.settings.local``
* Importar hojas_de_vida: 
  ``python ventanita/manage.py import_hojas_de_vida --tsvfile=dummy_data0.tsv --settings=ventanita.settings.local``
  
## Licencia
Este es un proyecto *open source* con una licencia permisiva (**WTFPL**, ver archivos
COPYING y LICENSE).
El derecho de autor (*copyright*) en este proyecto corresponde a varias personas.
El *copyright* para cada módulo está indicado al inicio de cada archivo, el cual
corresponde al autor inicial y personas que contribuyeron con adiciones y modificaciones.
