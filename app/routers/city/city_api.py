from fastapi import APIRouter
router = APIRouter()

from routers.city.City_class import City, db, City_Pydantic, CityIn_Pydantic


@router.get('/', tags=["city"]) 
def index():
    return {"title": "hello coder from city"}

@router.get('/list', tags=["city"])
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

@router.delete('/{city_id}', tags=["city"])
async def delete_city(city_id: int):
    await City.filter(id=city_id).delete()
    return {}