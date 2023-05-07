from fastapi import FastAPI

from .compositions import router as compositions_router
from .concerts import router as concerts_router
from .pianists import router as pianists_router
from .programs import router as programs_router

__all__ = ("register_routers",)


def register_routers(app: FastAPI):
    app.include_router(concerts_router)
    app.include_router(compositions_router)
    app.include_router(pianists_router)
    app.include_router(programs_router)
