FROM python:3.10.8-slim

ARG APP_ENV

EXPOSE 8080

ENV APP_ENV=${APP_ENV} \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=1 \
  PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_VERSION=1.2.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /preferred_item_service
COPY poetry.lock pyproject.toml /preferred_item_service/

RUN poetry install $(test "$APP_ENV" == "prod" && echo "--no-dev") --no-ansi --no-root

COPY . /preferred_item_service
CMD ["python", "-m", "preferred_item_service"]
