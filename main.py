import logging
from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from moneyed import list_all_currencies

app = FastAPI()

currency_codes = [currency.code for currency in list_all_currencies()]


class FilterParams(BaseModel):
    from_currency: Literal[tuple(currency_codes)]
    to_currency: Literal[tuple(currency_codes)]
    value: int


@app.get("/rates")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    logging.info(filter_query)
