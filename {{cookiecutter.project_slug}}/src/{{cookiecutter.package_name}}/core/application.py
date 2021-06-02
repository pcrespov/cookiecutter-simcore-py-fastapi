import logging
from typing import Optional

from fastapi import FastAPI

from ..meta import api_version, api_vtag
from ..api.module_setup import router as api_router

from .settings import AppSettings


logger = logging.getLogger(__name__)


def init_app(settings: Optional[AppSettings] = None) -> FastAPI:
    if settings is None:
        settings = AppSettings.create_default()

    logging.basicConfig(level=settings.loglevel)
    logging.root.setLevel(settings.loglevel)

    app = FastAPI(
        debug=settings.debug,
        title="Components Catalog Service",
        description="Manages and maintains a **catalog** of all published components (e.g. macro-algorithms, scripts, etc)",
        version=api_version,
        openapi_url=f"/api/{api_vtag}/openapi.json",
        docs_url="/dev/doc",
        redoc_url=None,  # default disabled
    )

    logger.debug(settings)
    app.state.settings = settings



    # app.add_exception_handler(HTTPException, http_error_handler)
    # app.add_exception_handler(RequestValidationError, http422_error_handler)

    # Routing
    app.include_router(api_router, prefix=f"/{api_vtag}")

    return app
