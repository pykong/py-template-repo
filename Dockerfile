# Stage 1: Configuring base image
FROM simbachain/poetry-3.11 AS base

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN python -m pip install --upgrade pip && \
    poetry config virtualenvs.create false && \
    poetry install --without dev,test --no-root

# Stage 2: Production environment with source code
FROM base AS production
COPY . /app
RUN poetry install --without dev,test

CMD ["poetry", "run", "app", "hello", "Ben"]
