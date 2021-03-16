all:
	@echo "Available commands: \n\
		make install : to install pipenv and other dependent packages \n\
		make superuser : creates a superuser to access the django admin \n\
		make dev : runs django development server \n\
		make run : run the django application \n\
		make shell : start a pipenv shell with all required packages available in the environment \n\
		make lint : runs linters on all project files and shows the changes \n\
		make test : run the test suite  \n\
		make coverage : runs tests and creates a report of the coverage \n\
		make clean : Clean up the db \n\
		make initialize-offline : Populate the DB from offline file \n\
		make initialize-online : Populate the DB by getting data from online \n\
 	"

install:
	python3 -m pip install pipenv
	pipenv install --dev
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate

dev:
	pipenv run python manage.py runserver

run: install
	# the default settings file is development, it can be changed
	# for any of the others, please don't use development setting in production
	export DJANGO_SETTINGS_MODULE='microservice.settings.development';\
	pipenv run gunicorn microservice.wsgi:application --bind localhost:8000

shell:
	@echo 'Starting pipenv shell. Press Ctrl-d to exit from the shell'
	pipenv shell

lint:
	# starts a pipenv shell, shows autopep8 diff and then fixes the files
	# does the same for isort
	@echo '---Running autopep8---'
	pipenv run autopep8 LocalFolioPOC -r -d
	pipenv run autopep8 LocalFolioPOC -r -i
	@echo '---Running isort---'
	pipenv run isort LocalFolioPOC --diff
	pipenv run isort LocalFolioPOC --atomic

coverage:
	@echo 'Running tests and making coverage files'
	pipenv run coverage run manage.py test
	pipenv run coverage report
	pipenv run coverage html
	@echo 'to see the complete report, open index.html on the htmlcov folder'

superuser:
	@echo 'creating superuser'
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
	User.objects.create_superuser('admin', 'admin@myproject.com', 'imagine')" \
	| pipenv run python manage.py shell
	@echo 'Username: admin , Password: imagine'

test:
	@echo 'Running tests'
	pipenv run python manage.py test

clean:
	@echo 'Flushing the db'
	pipenv run python manage.py flush

initialize-offline:
	@echo 'Import the data to DB from local file'
	pipenv run python manage.py initialize -l 1

initialize-online:
	@echo 'Import the data to DB from local file'
	pipenv run python manage.py initialize

