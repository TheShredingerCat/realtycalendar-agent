from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.agent_service import ask_agent
from app.services.gdrive_service import find_tool_by_name

router = APIRouter(prefix="/agent", tags=["AI Agent"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/chat", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.get("/ask")
def ask(q: str = Query(..., description="Вопрос пользователя")):
    """ИИ-ответ на основе таблицы + страницы инструмента."""
    answer = ask_agent(q)
    return {"answer": answer}

@router.get("/debug")
def debug(q: str = Query(..., description="Тест запроса")):
    """Возвращает: найденный инструмент и краткий ответ."""
    tool = find_tool_by_name(q)
    if not tool:
        return {"status": "no_tool", "msg": "Инструмент не найден в таблице"}
    answer = ask_agent(q)
    return {"status": "ok", "tool": tool, "answer": answer}
