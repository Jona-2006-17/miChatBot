from fastapi import FastAPI
from app.router import chatBot


app = FastAPI()


app.include_router(chatBot.router, prefix="/chat", tags=["chat"])
app.include_router(chatBot.router, prefix="/whatsapp" tags=["WhatsApp"])





@app.get("/")
async def root():
    return {"message": "Hello World"}