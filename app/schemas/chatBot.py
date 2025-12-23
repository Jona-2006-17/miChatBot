from pydantic import BaseModel

class ChatMessage(BaseModel):
    mensaje: str
    