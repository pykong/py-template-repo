# Stage 1: Base image; exporting wheel
FROM python:3.12-slim-bookworm AS builder

# Set environment variables
ENV POETRY_VIRTUALENVS_CREATE=false

# Install pipx
RUN python3 -m pip install -U --no-cache-dir pipx && \
    pipx ensurepath

# Install Poetry via pipx
RUN pipx install --global poetry

# Set work directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY . ./

# Install dependencies and build the wheel
RUN poetry install \
    --no-root \
    --no-directory \
    --without dev,test \
    --no-interaction \
    --no-ansi

RUN poetry build -f wheel --no-interaction --no-ansi


# Stage 2: Runner image, installing wheel, running the application
FROM python:3.12-slim-bookworm AS runner

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Set work directory
WORKDIR /src

# Copy the built wheel from the builder stage
COPY --from=builder /app/dist/*.whl ./

# Install the wheel
RUN pip install --no-cache-dir *.whl

# Copy application code
COPY . .

CMD ["python", "-m", "src", "hello", "Ben"]
