import os
import requests
import pandas as pd
from openai import OpenAI
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargar configuración desde variables de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')
API_KEY = os.getenv('OPENAI_API_KEY')

# Configurar APIs
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
client = OpenAI(api_key=API_KEY)
model = "gpt-4o-mini"

# Tu menú y contexto (igual que antes)
MENU = {
    "helado": {
        "1/4 kilo": 2500,
        "1/2 kilo": 4000,
        "1 kilo": 7000,
    },
    "sabores": [
        "Dulce de leche", "Dulce de leche granizado", "Dulce de leche con almendras",
        "Chocolate", "Chocolate amargo", "Chocolate suizo",
        "Banana split", "Frutilla", "Frutilla a la crema",
        "Vainilla", "Limón", "Menta granizada"
    ],
    "toppings": {
        "Rocklets": 500,
        "Kit Kat": 700,
        "Oreo": 350,
    }
}

contextos = {}

def get_user_context(chat_id):
    if chat_id not in contextos:
        contextos[chat_id] = [{
            'role': 'system',
            'content': f"""
Eres OrderBot, un servicio automatizado para recolectar pedidos para Helados,
una heladería local llamada LIMAR ubicada en Av La Plata al 1500. Primero saludas al cliente, y muestra el menú y los precios.
luego recolectas el pedido teniendo en cuenta no ofrecer ni vender nada que no este específicado en el contexto.
Esperas para recolectar todo el pedido, permitiendo que agregue más helado o cualquier otra cosa del menú las veces que sea necesario.
Finalmente, cuando ya recolectaste el pedido, confirmas con el usuario la lista completa del pedido con su cuenta total y pides que si hay errores te informen.
Luego preguntas si pagará en efectivo o tarjeta y finalmente preguntas si es para recoger o para entregar. Si es una entrega, pides dirección.
Finalmente, escribes literalmente: 'Los empleados le confirmarán el total (por si haya un error en mis cálculos) y le cobrarán.'

Menú:
- Cuarto kilo de helado: ${MENU['helado']['1/4 kilo']}
- Medio kilo de helado: ${MENU['helado']['1/2 kilo']}
- Un kilo de helado: ${MENU['helado']['1 kilo']}

Sabores: {", ".join(MENU['sabores'])}

Toppings:
{chr(10).join([f"- {t}: ${MENU['toppings'][t]}" for t in MENU['toppings']])}
"""
        }]
    return contextos[chat_id]

def send_message(text, chat_id):
    try:
        response = requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": text})
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
        return False

def process_message(user_message, chat_id):
    context = get_user_context(chat_id)
    context.append({'role': 'user', 'content': user_message})

    try:
        response = client.chat.completions.create(
            model=model, messages=context
        )
        bot_reply = response.choices[0].message.content
        send_message(bot_reply, chat_id)
        context.append({'role': 'assistant', 'content': bot_reply})

        if "Los empleados le confirmarán el total" in bot_reply:
            # Guardar en base de datos o archivo (adaptar para Spaces)
            save_order(chat_id, bot_reply)
            
    except Exception as e:
        send_message("❌ Lo siento, hubo un error procesando tu mensaje.", chat_id)

def save_order(chat_id, content):
    # Para Spaces, podrías usar una base de datos simple o logging
    print(f"Pedido guardado - Chat ID: {chat_id}, Contenido: {content}")

# Webhook para Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        user_message = update['message'].get('text', '')
        
        if user_message:
            process_message(user_message, chat_id)
    
    return jsonify({'status': 'ok'})

# Endpoint principal para Hugging Face
@app.route('/')
def home():
    return "🤖 Bot de Telegram funcionando correctamente!"

# Para desarrollo local
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)