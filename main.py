from typing import Annotated
from fastapi import FastAPI, Query
from moneyed import list_all_currencies
from pydantic import BaseModel, field_validator

app = FastAPI()

currency_codes = [currency.code for currency in list_all_currencies()]


class FilterParams(BaseModel):
    from_currency: str = Query(alias='from')
    to_currency: str = Query(alias='to')
    value: int

    @field_validator('from_currency', 'to_currency')
    def validate_currency(cls, value: str):
        if value not in currency_codes:
            raise ValueError(
                f"The value must be one of the valid currency codes defined in "
                f"ISO 4217 Currencies (except North Korean Won): {', '.join(currency_codes)}"
            )
        return value


@app.get("/api/rates")
async def read_items(filtered_query: Annotated[FilterParams, Query()]):
    print(filtered_query)

