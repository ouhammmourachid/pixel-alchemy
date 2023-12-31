.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall && poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: collectstatic
collectstatic:
	poetry run python manage.py collectstatic

.PHONY: build
build:
	docker compose build

.PHONY: up
up:
	docker compose up

.PHONY: build-up
build-up:build up;
