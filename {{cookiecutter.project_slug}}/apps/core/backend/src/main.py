from fastapi import FastAPI
from core.backend.src.apps_loader import load_app

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    print("Loading apps...")
    load_app()