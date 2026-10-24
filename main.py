import config  # noqa: F401  (loads .env first)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import database
from routes import auth, resume, interview, roadmap

database.init()
app = FastAPI(title="PlaceReady")
for r in (auth, resume, interview, roadmap):
    app.include_router(r.router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")  # serves the web page
