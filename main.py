import os
import httpx
from decimal import Decimal, ROUND_HALF_UP

from dotenv import load_dotenv
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from moneyed import list_all_currencies
from pydantic import BaseModel, field_validator
from typing import Annotated


load_dotenv()
api_key = os.getenv('API_CODE')

CURRENCY_RATES_SERVICE_URL_SCHEME = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
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
async def convert_currency(filtered_query: Annotated[FilterParams, Query()]):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                CURRENCY_RATES_SERVICE_URL_SCHEME.format(
                    api_key=api_key,
                    from_currency=filtered_query.from_currency
                )
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

        # Get exchange rates from the response data
        exchange_rates = data['conversion_rates']

        # Validate if the from_currency exists in the exchange rates
        if filtered_query.from_currency not in exchange_rates:
            raise HTTPException(status_code=404, detail="The currency was not found in the vendor API")

        rate = exchange_rates[filtered_query.to_currency]
        # print(f'rate {rate}')
        precise_rate = Decimal(str(rate))
        # print(f'precise_rate {precise_rate}')
        rounded_precise_rate = precise_rate.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        # print(f'rounded_precise_rate {rounded_precise_rate}')
        result = float(rounded_precise_rate * filtered_query.value)
        return JSONResponse(
            content={"result": result},
            )

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch exchange rates")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

