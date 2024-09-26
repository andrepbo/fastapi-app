# FastAPI Application

This is a FastAPI application with Docker support, and it includes testing functionality using `pytest`.

## Features

- FastAPI server running with Uvicorn
- Dockerized for easy deployment
- Testing setup using `pytest`
- Automatic testing container setup with Docker

## Requirements

The following packages are required for the project:

- `fastapi`
- `uvicorn`
- `pytest`
- `httpx`

These dependencies are listed in the `requirements.txt` file.

## Setup Instructions

### Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### Install Dependencies

To install the dependencies, you can use `pip` with the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Docker Setup

This project uses Docker and Docker Compose for running the application and tests. Make sure you have Docker installed on your system.

To build and run the application using Docker:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:5001`.

### Running Tests

You can run the tests in a separate Docker container using the following command:

```bash
docker-compose run test
```

This will execute the tests located in `test_app.py`.

## Configuration

The environment variables are configured within the `docker-compose.yml` file. Important variables include:

- `FASTAPI_APP`: The entry point for the FastAPI application (`app.py`).
- `FASTAPI_RUN_HOST`: Host configuration for running the FastAPI app (`0.0.0.0`).

## File Overview

- `app.py`: The main FastAPI application file.
- `test_app.py`: The file containing tests using `pytest`.
- `Dockerfile`: Docker instructions for setting up the application container.
- `docker-compose.yml`: Docker Compose configuration for running the application and test services.