from fastapi import APIRouter

from .routes import items, health, meta

router = APIRouter()
router.include_router(health.router)

# API
router.include_router(meta.router, tags=["meta"], prefix="/meta")
router.include_router(items.router, tags=["items"], prefix="/items")
