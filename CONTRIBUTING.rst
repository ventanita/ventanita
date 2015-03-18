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
4. Subir los cambios a tu copia del repositorio: ``git push origin patch-1``
5. Estando en Github, crear un *pull request*.
6. Fastidiar a AniversarioPeru para que acepte el *pull request*.

Antes de hacer *pull request* adicionales
-----------------------------------------

1. Ir a tu rama master (*master branch*): ``git checkout master``
2. Agregar a tu repositorio el *upstream repo URL*: ``git remote add upstream https://github.com/aniversarioperu/ventanita.git``
3. Actualizar tu copia del repositorio: ``git fetch upstream``
4. ``git merge upstream/master``
5. Repetir las instrucciones de arriba desde el paso 2.
