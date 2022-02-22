devreset:
	docker-compose build app
	docker-compose up -d db-tree
	#docker-compose run --rm app python manage.py collectstatic --noinput
	make createsuperuser
runserver:
	docker-compose run --rm --service-ports app python manage.py runserver 0.0.0.0:8000
migrations:
	docker-compose run app ./manage.py makemigrations
migrate:
	docker-compose run app ./manage.py migrate
createsuperuser:
		docker-compose run app python manage.py shell -c "from apps.accounts.models import User; \
			u, _ = User.objects.get_or_create(email='dev@plantree.com'); \
			u.username = 'dev'; \
			u.set_password('dev123'); \
			u.is_superuser = u.is_staff = True; \
			u.save(); \
			print('Superuser: dev@plantree.com / dev123');"
clean:
	docker-compose kill && docker-compose down --rmi all
	sudo rm -rf data/
	sudo rm -rf staticfiles/
	sudo rm -rf media/
shell:
	docker-compose run app python manage.py shell_plus --ipython
