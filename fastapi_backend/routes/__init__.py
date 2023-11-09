from fastapi import APIRouter

from .v1 import v1_router

main_router = APIRouter()

main_router.include_router(v1_router, prefix="/v1", tags=["v1"])

@main_router.get("/")
async def index():
    return {"message": "Hello World!"}
