from fastapi import FastAPI
from app.router import chatBot


app = FastAPI()


app.include_router(chatBot.router, prefix="/chat", tags=["chat"])





@app.get("/")
async def root():
    return {"message": "Hello World"}