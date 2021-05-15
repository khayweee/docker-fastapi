from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist
router = APIRouter()

from routers.city.City_class import City, db, City_Pydantic, CityIn_Pydantic


class Status(BaseModel):
    message: str

@router.get('/', tags=["city"]) 
def index():
    return {"title": "hello coder from city"}

@router.get('/list', tags=["city"], response_model=List[City_Pydantic])
async def list_cities():
    return await City_Pydantic.from_queryset(City.all())

@router.get('/{city_id}', tags=["city"])
async def get_city(city_id: int):
    return await City_Pydantic.from_queryset_single(City.get(id=city_id))

@router.post('/', tags=["city"])
async def create_city(city: CityIn_Pydantic):
    """ Creare a city in DB """
    # FastAPI will require an input of City class 
    city_obj = await City.create(**city.dict(exclude_unset=True))
    return await City_Pydantic.from_tortoise_orm(city_obj)

@router.delete('/{city_id}', tags=["city"],  response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_city(city_id: int):
    try:
        city_obj = await City_Pydantic.from_queryset_single(City.get(id=city_id))
        deleted_count = await City.filter(id=city_id).delete()
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"City {city_id} not found")
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"City {city_id} not found")
    return Status(message=f"Deleted city {city_obj.name}")
