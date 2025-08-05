from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.chatbot import generate_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        reply = generate_response(request.message)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
