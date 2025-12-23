from fastapi import APIRouter
from app.bot.procesador import responder, analizar_texto
from app.schemas.chatBot import ChatMessage
router = APIRouter()

@router.post("/chat")
def chat(data: ChatMessage):
    respuesta = responder(data.mensaje)
    return {"Respuesta: ": respuesta}


@router.post("/analizar")
def analizar(data: ChatMessage):
    info = analizar_texto(data.mensaje)
    return info

