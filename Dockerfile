# Stage 1: Base image; exporting wheel
FROM python:3.11-slim-bookworm AS wheel-builder

# Set environment variables
ENV POETRY_VIRTUALENVS_CREATE=false

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install dependencies and build the wheel
RUN poetry install --no-root --without dev,test && \
    poetry build -f wheel


# Stage 2: Runner image, installing wheel, running the application
FROM python:3.11-slim-bookworm AS runner

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy the built wheel from the builder stage
COPY --from=wheel-builder /app/dist/*.whl ./

# Install the wheel
RUN pip install --no-cache-dir *.whl

# Copy application code
COPY . .

CMD ["poetry", "run", "cli", "hello", "Ben"]
