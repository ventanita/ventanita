migrations:
	python ventanita/manage.py makemigrations --settings=ventanita.settings.local
	python ventanita/manage.py migrate --settings=ventanita.settings.local

serve:
	python ventanita/manage.py runserver --settings=ventanita.settings.local
