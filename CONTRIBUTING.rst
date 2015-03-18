Recomendaciones a los colaboradores
===================================

La lista de tareas para hacer están marcadas según nivel de dificultad:
`<https://github.com/aniversarioperu/ventanita/issues>`_.
Si tienes ideas o encuentras cosas para corregir, mejorar, bugs, puedes crear
nuevos *issues* o comentar en los existentes.

Flujo de trabajo recomendado
----------------------------

1. Hacer fork del repositorio usando tu cuenta Github.
2. Crear una nueva rama (*branch*): ``git checkout -b patch-1``
3. Agregar código, corregir bugs, etc.
4. Agregar la nota de *copyright* al inicio de cada archivo (si no está). En caso
   ya exista esta nota puedes agregar tu nombre si has modificado el archivo.
   Usar este modelo::

    # Copyright 2015 by Fulano Mengano. All rights reserved.
    # Revisions 2015 copyright by Zutano Perengano. All rights reserved.
    # This code is part of the Ventanita distribution and governed by its
    # license.  Please see the LICENSE file that should have been included
    # as part of this package.

5. Subir los cambios a tu copia del repositorio: ``git push origin patch-1``
6. Estando en Github, crear un *pull request*.
7. Fastidiar a AniversarioPeru para que acepte el *pull request*.
8. Agregas tu nombre y email de contacto al archivo ``CREDITS``.

Antes de hacer *pull request* adicionales
-----------------------------------------

1. Ir a tu rama master (*master branch*): ``git checkout master``
2. Agregar a tu repositorio el *upstream repo URL*: ``git remote add upstream https://github.com/aniversarioperu/ventanita.git``
3. Actualizar tu copia del repositorio: ``git fetch upstream``
4. ``git merge upstream/master``
5. Repetir las instrucciones de arriba desde el paso 2.
