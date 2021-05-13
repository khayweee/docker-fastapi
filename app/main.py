from fastapi import FastAPI
from core.city import City
app = FastAPI()

db = []

@app.get("/")
def index():
    return {"title": "hello coder"}

@app.get('/cities')
def get_cities():
    return db

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]

@app.post('/cities')
def create_city(city: City):
    """ Creare a city in DB """
    # FastAPI will require an input of City class 
    db.append(city.dict())
    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
