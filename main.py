from fastapi import FastAPI

from routers.status import router as status_router
from routers.weather.current import router as current_weather_router
from routers.weather.historical import router as historical_weather_router

app = FastAPI()

app.include_router(status_router)
app.include_router(current_weather_router)
app.include_router(historical_weather_router)
