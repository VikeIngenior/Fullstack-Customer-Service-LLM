from langchain.chat_models import init_chat_model

from app.llm.base import BaseLLM

from dotenv import load_dotenv

load_dotenv()

class GroqLLM(BaseLLM):
    def __init__(self):
        self.model = init_chat_model("llama3-8b-8192", model_provider="groq")

    def ask(self, question: str) -> str:
        return self.model.invoke(question)
