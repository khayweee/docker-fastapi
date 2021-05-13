from fastapi import APIRouter
from routers.city.City_class import City, db

router = APIRouter()

@router.get('/', tags=["city"]) 
def index():
    return {"title": "hello coder from city"}

@router.get('/list', tags=["city"])
def get_cities():
    return db

@router.get('/{city_id}', tags=["city"])
def get_city(city_id: int):
    return db[city_id-1]

@router.post('/', tags=["city"])
def create_city(city: City):
    """ Creare a city in DB """
    # FastAPI will require an input of City class 
    db.append(city.dict())
    return db[-1]

@router.delete('/{city_id}', tags=["city"])
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}