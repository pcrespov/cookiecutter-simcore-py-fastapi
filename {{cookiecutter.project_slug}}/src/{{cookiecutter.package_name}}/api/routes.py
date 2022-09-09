"""
    api app module
"""
from fastapi import APIRouter, FastAPI
from .._meta import api_vtag
from . import _healthcheck


def setup_api(app: FastAPI):
    router = APIRouter()

    # FIXME: _healthcheck
    app.include_router(router, prefix=f"/{api_vtag}")
