import httpx
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from decimal import Decimal, ROUND_HALF_UP
from app.config import settings
from app.models import FilterParams
from typing import Annotated

router = APIRouter()


@router.get("/api/rates")
async def convert_currency(filtered_query: Annotated[FilterParams, Query()]):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                settings.currency_rates_service_url.format(
                    api_code=settings.api_code,
                    from_currency=filtered_query.from_currency
                )
            )
            response.raise_for_status()
            data = response.json()

        exchange_rates = data['conversion_rates']

        if filtered_query.from_currency not in exchange_rates:
            raise HTTPException(status_code=404, detail="The currency was not found in the vendor API")

        rate = exchange_rates[filtered_query.to_currency]
        precise_rate = Decimal(str(rate)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        result = float(precise_rate * filtered_query.value)

        return JSONResponse(content={"result": result})

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Failed to fetch exchange rates")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
