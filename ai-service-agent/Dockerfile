# Set Python and Poetry versions as build arguments
ARG PYTHON_VERSION=3.13
ARG POETRY_VERSION=2.1.3

FROM python:${PYTHON_VERSION} AS build
ARG POETRY_VERSION

# Set working directory
WORKDIR /usr/src

# Copy all files into /usr/src
COPY . .

# Install Poetry, the Python dependency manager
RUN pip install poetry==${POETRY_VERSION}

# Install project dependencies defined in pyproject.toml
RUN poetry install

ENV PYTHONPATH=/usr/src/src
WORKDIR /usr/src/src

# Run project from inside src/, and import main as “main:app”
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]