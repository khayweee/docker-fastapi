from pydantic import BaseModel


class City(BaseModel):
    """ Specify how a city is represented """
    # Fields in City
    # Specify the type of variable
    name: str
    timezone: str