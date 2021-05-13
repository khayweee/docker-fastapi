from fastapi import APIRouter
from routers.city.city_api import router as city_router


router = APIRouter()

router.include_router(
    city_router,
    prefix='/cities',
    tags=['city'],
)