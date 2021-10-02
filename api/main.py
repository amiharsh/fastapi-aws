from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def list_items():
    return {"items": "Apple"}

handler = Mangum(app=app)
