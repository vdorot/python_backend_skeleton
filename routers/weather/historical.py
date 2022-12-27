from fastapi import APIRouter

router = APIRouter(
    prefix="/weather/historical",
    tags=["weather"]
)
