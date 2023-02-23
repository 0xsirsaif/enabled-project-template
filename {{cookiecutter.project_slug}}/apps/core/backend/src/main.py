from fastapi import FastAPI
from core.backend.src.apps_loader import get_sub_apps


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    print("Loading apps...")
    apps = get_sub_apps()
    # include sub-apps routes
    for sub_app in apps:
        app.include_router(sub_app.app)
