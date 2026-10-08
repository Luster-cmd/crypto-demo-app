import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Crypto Bot Demo Mini App")
WEB_DIR = os.path.join(os.path.dirname(__file__), "web")
app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(os.path.join(WEB_DIR, "index.html"))


@app.get("/health")
def health():
    return {"ok": True, "mode": "demo"}
