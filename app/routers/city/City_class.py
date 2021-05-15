import requests
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from .city_api import router

db = []

class City(Model):
    """ Specify how a city is represented """
    # Fields in City
    # Specify the type of variable
    id = fields.IntField(pk=True)
    name = fields.CharField(50, unique=True)
    timezone = fields.CharField(50)

    def current_time(self) -> str:
        """ A field that requires computation """
        r = requests.get(f'http://worldtimeapi.org/api/timezone/{self.timezone}')
        current_time = r.json()['datetime']
        return current_time
    
    class PydanticMeta:
        """ ensures new fields are computed and its a readonly field """
        computed = ('current_time', )
        # exclude = ('timezone', )

City_Pydantic = pydantic_model_creator(City, name='City')
# CityIn will be used for data coming in
CityIn_Pydantic = pydantic_model_creator(City, name='CityIn', exclude_readonly=True)

register_tortoise(
    router,
    db_url='sqlite://database/city_db.sqlite3',
    modules={'models': ['routers.city.City_class']},
    generate_schemas=True
)