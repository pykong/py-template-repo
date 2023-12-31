# Stage 1: Configuring base image
FROM simbachain/poetry-3.12 AS base

WORKDIR /src

COPY pyproject.toml .
COPY poetry.lock .

RUN python -m pip install --upgrade pip && \
    poetry config virtualenvs.create false && \
    poetry install --without dev,test --no-root

# Stage 2: Production environment with source code
FROM base AS production
COPY . /src
RUN poetry install --without dev,test

CMD ["poetry", "run", "cli", "hello", "Ben"]
