migrations:
	python ventanita/manage.py makemigrations --settings=ventanita.settings.local
	python ventanita/manage.py migrate --settings=ventanita.settings.local

serve:
	python ventanita/manage.py runserver --settings=ventanita.settings.local

test:
	coverage run --source ventanita ventanita/manage.py test -v 2 \
	    pages \
	    --settings=ventanita.settings.testing

coverage: test
	coverage report -m
	coverage html
