from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.llm.groq_llm import GroqLLM

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
llm = GroqLLM()

@router.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    raw_answer = llm.ask(question)
    answer = raw_answer.content
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})