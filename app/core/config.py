from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    DATABASE_URI: str = "sqlite:///./sql_app.db"
    ELASTIC_APM_VERIFY_SERVER_CERT: bool = True
    ELASTIC_APM_SERVICE_NAME: str = "tracing_default"
    ELASTIC_APM_SERVER_URL: Optional[AnyHttpUrl]  # default: 'http://localhost:8200'
    ELASTIC_APM_ENVIRONMENT: str = "prod_default"
    ELASTIC_APM_GLOBAL_LABELS: str = (
        "platform=DemoPlatform, application=DemoApplication"
    )

    class Config:
        case_sensitive = True


settings = Settings()
