# Currency Conversion API

A simple FastAPI application for converting currency rates using exchange rates from an external API: 
https://www.exchangerate-api.com/

The application accepts currency conversion requests and returns the converted values based on the latest exchange rates.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Docker](#docker)

## Features

- Currency conversion based on real-time exchange rates.
- Supports various currencies defined in ISO 4217.
- Validates input parameters for currency codes.
- Returns results in JSON format.

## Technologies Used

- [Python](https://www.python.org/) - Programming Language, you can use python 3.10
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework for building APIs
- [httpx](https://www.python-httpx.org/) - HTTP client for async requests
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management
- [Moneyed](https://py-moneyed.readthedocs.io/en/latest/) - Handling currency codes
- [dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/MalyshevDenSer/currency-conversion-api.git
    cd currency-conversion-api
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    ### Windows:

    ```bash
    venv\Scripts\activate
    ```

    ### macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env`  file using the `.env.example` file from the repository to include your API credentials

    ```bash
   API_CODE=your_api_code
   CURRENCY_RATES_SERVICE_URL=https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}
    ```

## Usage

To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --reload
   ```

Once the server is running, you can access the API documentation at:

```bash
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /api/rates
Converts currency from one type to another.

#### Query Parameters
- `from`: The currency code to convert from (e.g., USD).
- `to`: The currency code to convert to (e.g., RUB).
- `value`: The amount in the from currency to convert.

#### Example Request

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=1'
```

#### Example Response

```
{
  "result": 95.45
}
```

## Configuration

Make sure to set the following environment variables in your `.env` file:

- API_CODE: To get it, sign in: https://app.exchangerate-api.com/dashboard
- CURRENCY_RATES_SERVICE_URL: The URL template for fetching the latest currency rates.

## Docker

This project can be containerized using Docker, which allows you to easily deploy and run the application in an isolated environment. Below are the steps to build and run the application using Docker.

### Prerequisites

- [Docker](https://www.docker.com/) must be installed on your machine.

### Building the Docker Image

1. Ensure you're in the root directory of the project (where the `Dockerfile` is located).
2. Build the Docker image by running the following command:

   ```bash
   docker build -t currency-conversion-api .
   ```
   
This command will create a Docker image named currency-conversion-api by following the instructions in the `Dockerfile`.

### Running the Docker Container

Once the image is built, run a container using the following command:

```
docker run -d -p 8000:8000 currency-conversion-api
```

This will start the application in detached mode (-d), mapping port 8000 from the container to port 8000 on your local machine.

You can now access the FastAPI application at:

```
http://127.0.0.1:8000
```

### Stopping the Docker Container

To stop the running container, you can list the running containers with:

```bash
docker ps
```

Then stop it using the container ID:

```bash
docker stop <container_id>
```

### ???

### PROFIT!
