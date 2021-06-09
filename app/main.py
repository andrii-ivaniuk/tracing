from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI

from app.api.v1.main import api_router
from app.core.config import settings
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Try tracing")

if settings.ELASTIC_APM_SERVER_URL:
    apm = make_apm_client(
        {
            "VERIFY_SERVER_CERT": settings.ELASTIC_APM_VERIFY_SERVER_CERT,
            "SERVICE_NAME": settings.ELASTIC_APM_SERVICE_NAME,
            "SERVER_URL": settings.ELASTIC_APM_SERVER_URL,
            "ENVIRONMENT": settings.ELASTIC_APM_ENVIRONMENT,
            "GLOBAL_LABELS": settings.ELASTIC_APM_GLOBAL_LABELS,
        }
    )
    app.add_middleware(ElasticAPM, client=apm)

app.include_router(api_router, prefix=settings.API_PREFIX)
