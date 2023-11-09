from fastapi import APIRouter

v1_router = APIRouter()

@v1_router.get("/")
async def index():
    return {"version": "v1"}
