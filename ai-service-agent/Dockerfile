# Set Python and Poetry versions as build arguments
ARG PYTHON_VERSION=3.14
ARG POETRY_VERSION=2.1.3

# Use the official Python image as the base image
FROM python:${PYTHON_VERSION} AS build

# Set working directory
WORKDIR /usr/src

# Copy the project dependencies file to poetry usage
COPY pyproject.toml ./

# Install Poetry, the Python dependency manager
RUN pip install poetry==${POETRY_VERSION}

# Install project dependencies defined in pyproject.toml
RUN poetry install

# Copy all files into /usr/src
COPY . .

ENV PYTHONPATH=/usr/src/src
CMD ["poetry", "run", "python", "-m", "src.main"]
