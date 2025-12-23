from fastapi import APIRouter, Response
from app.bot.procesador import responder, analizar_texto
from app.schemas.chatBot import ChatMessage
from fastapi import Request

from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

@router.post("/chat")
def chat(data: ChatMessage):
    respuesta = responder(data.mensaje)
    return {"Respuesta: ": respuesta}


@router.post("/analizar")
def analizar(data: ChatMessage):
    info = analizar_texto(data.mensaje)
    return info

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    mensaje_usuario = form_data.get("Body")

    respuesta_bot = responder(mensaje_usuario)

    twilio_resp = MessagingResponse()

    twilio_resp.message(respuesta_bot)

    return Response(content=str(twilio_resp), media_type="application/xml")

