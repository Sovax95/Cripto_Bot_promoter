
from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.get("/")
async def read_root():
    return {"message": "CryptoBot Promoter API rodando na nuvem 🚀"}

@app.post("/notificar")
async def notificar_usuario(request: Request):
    data = await request.json()
    mensagem = data.get("mensagem", "Mensagem não fornecida.")
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensagem
        }
        response = requests.post(url, json=payload)
        return {"status": "enviado", "detalhes": response.json()}
    else:
        return {"erro": "Token ou Chat ID não configurado"}
