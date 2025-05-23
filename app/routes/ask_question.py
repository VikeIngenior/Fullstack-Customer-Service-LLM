from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    answer = "This is a test answer"
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})