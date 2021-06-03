"""
    api app module
"""
from fastapi import APIRouter, FastAPI
from ..meta import api_vtag
from .routes import status, health, meta



def setup_api(app: FastAPI):
    router = APIRouter()

    #
    router.include_router(health.router)

    router.include_router(meta.router, tags=["meta"], prefix="/meta")
    router.include_router(status.router, tags=["status"], prefix="/diagnostics")

    app.include_router(router, prefix=f"/{api_vtag}")
