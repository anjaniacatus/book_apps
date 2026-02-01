#!/usr/bin/env bash
set -o errexit
uv sync
uv run python manage.py migrate
# create superuser without ssh access on render
if [ "$CREATE_SUPERUSER" = "True" ]; then
  python manage.py createsuperuser --noinput
fi

uv run python manage.py collectstatic --no-input
uv run python manage.py test
