import logging
from fastapi import FastAPI
from app.routes.currency import router as currency_router

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Include the currency router
app.include_router(currency_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Currency Conversion API!"}
