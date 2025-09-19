from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.gdrive_service import get_all_rows

router = APIRouter(prefix="/gdrive", tags=["Google Drive"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/read")
def read_excel():
    """JSON-выдача: [{tool, url}, ...]"""
    data = get_all_rows()
    if isinstance(data, dict) and data.get("error"):
        raise HTTPException(status_code=500, detail=data["error"])
    return {"rows": data}

@router.get("/ui", response_class=HTMLResponse)
def gdrive_table(request: Request):
    """Страница-таблица с поиском/сортировкой."""
    return templates.TemplateResponse("gdrive.html", {"request": request})
