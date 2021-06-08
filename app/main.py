from fastapi import FastAPI

from app.api.v1.main import api_router
from app.core.config import settings
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Try tracing")

app.include_router(api_router, prefix=settings.API_PREFIX)
