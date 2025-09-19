import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.routes import gdrive, agent
from fastapi.staticfiles import StaticFiles


load_dotenv(override=True)
app = FastAPI(title="RealtyCalendar Demo", version="1.0.0")

# CORS для фронтов/веб-UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gdrive.router)
app.include_router(agent.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")

@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"status": "ok"}
