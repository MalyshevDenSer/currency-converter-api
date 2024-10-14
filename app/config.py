from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_code: str
    currency_rates_service_url: str

    class Config:
        env_file = ".env"


settings = Settings()
