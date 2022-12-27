from fastapi import APIRouter

router = APIRouter(
    prefix="/weather/current",
    tags=["weather"]
)
