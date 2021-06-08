from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX = "/api/v1"
    DATABASE_URI = "sqlite:///./sql_app.db"

    class Config:
        case_sensitive = True


settings = Settings()
