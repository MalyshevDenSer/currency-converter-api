FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

# Define environment variables (optional, can also be set in .env file)
# ENV API_CODE=your_api_code
# ENV CURRENCY_RATES_SERVICE_URL=https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}

# Optionally, set environment variables from a .env file at runtime
# Use this line in your docker-compose.yml or when running the container

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]