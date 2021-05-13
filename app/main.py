from fastapi import FastAPI
from routers import city

app = FastAPI()

app.include_router(
    city.router,
    prefix="/api/city"
)

@app.get("/")
def index():
    return {"title": "hello coder"}