# Stage 1: Base image; exporting wheel
FROM python:3.11-slim-bookworm AS base

WORKDIR /src

COPY pyproject.toml .
COPY poetry.lock .

# TODO: Complete image; right now it is not working

# TODO: Pin Poetry version
RUN python -m pip install --upgrade pip && \
    poetry config virtualenvs.create false && \
    poetry install --without dev,test --no-root

# Stage 2: Runner image, installing wheel
FROM python:3.11-slim-bookworm AS runner
COPY . /src
RUN poetry install --without dev,test

CMD ["poetry", "run", "cli", "hello", "Ben"]
