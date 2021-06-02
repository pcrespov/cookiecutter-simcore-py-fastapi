"""
    api app module
"""
from fastapi import APIRouter

from .routes import status, health, meta

router = APIRouter()
router.include_router(health.router)

# API
router.include_router(meta.router, tags=["meta"], prefix="/meta")
router.include_router(status.router, tags=["status"], prefix="/diagnostics")
