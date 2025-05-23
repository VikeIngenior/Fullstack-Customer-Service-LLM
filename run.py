from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn

from app.routes import homepage, ask_question

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(homepage.router)
app.include_router(ask_question.router)

if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)
