from fastapi import APIRouter

from app.routes.v1.endpoints import health, items

endpoint_router = APIRouter()

endpoint_router.include_router(
    health.router, prefix="", tags=["Health"]
)

endpoint_router.include_router(
    items.router, prefix="/api/v1", tags=["Items"]
) 