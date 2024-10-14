import logging
from fastapi import FastAPI
from app.routes.currency import router as currency_router

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

app.include_router(currency_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Currency Conversion API!"}
