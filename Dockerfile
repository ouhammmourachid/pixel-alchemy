FROM python:3.11.4-buster

WORKDIR /opt/project

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV MISS_JANNAT_SETTINGS_IN_DOCKER true


RUN set -xe \
    && apt-get update \
    && apt-get install build-essential \
    && pip install pip==23.0 virtualenvwrapper poetry==1.6.1

# For image build time optimization purposes we install depdendencies here (so changes in the source code will not
# require dependencies reinstallation)
COPY ["pyproject.toml", "poetry.lock", "./"]
RUN poetry run pip install pip==23.0
RUN poetry run pip install daphne


RUN poetry install --no-root

COPY ["README.md", "Makefile", "./"]
COPY accounts accounts
COPY media media
COPY ModelLog ModelLog
COPY PixelAlchemy PixelAlchemy
COPY store store
COPY manage.py manage.py
RUN poetry install  # this installs just the source code itself, since dependencies are installed before

COPY scripts/dockerized-core-run.sh ./run.sh
RUN chmod a+x run.sh
ENTRYPOINT ["./run.sh"]
