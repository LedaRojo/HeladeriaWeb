import os
import gradio as gr
from openai import OpenAI

# Configuración de API
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
model = "gpt-4o-mini"

# Menú de heladería
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

# Contextos por sesión
def get_system_prompt():
    return {
        'role': 'system',
        'content': f"""
Eres OrderBot, un servicio automatizado para recolectar pedidos para Helados,
una heladería local llamada LIMAR ubicada en Av La Plata al 1500. Primero saludas al cliente y muestras el menú con precios.
Recolecta el pedido sin ofrecer nada fuera de este menú.
Permite que el cliente agregue más productos.
Cuando el pedido esté completo, confirma la lista con el total y pregunta forma de pago (efectivo o tarjeta).
Luego pregunta si es para recoger o entregar. Si es entrega, pide dirección.
Finalmente, escribe literalmente: 'Los empleados le confirmarán el total (por si haya un error en mis cálculos) y le cobrarán.'

Menú:
- Cuarto kilo de helado: ${MENU['helado']['1/4 kilo']}
- Medio kilo de helado: ${MENU['helado']['1/2 kilo']}
- Un kilo de helado: ${MENU['helado']['1 kilo']}

Sabores: {", ".join(MENU['sabores'])}

Toppings:
{chr(10).join([f"- {t}: ${MENU['toppings'][t]}" for t in MENU['toppings']])}
"""
    }

# Procesar conversación
def chat_with_bot(message, history):
    history_openai = [get_system_prompt()]
    for user, bot in history:
        history_openai.append({"role": "user", "content": user})
        if bot:
            history_openai.append({"role": "assistant", "content": bot})

    history_openai.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=history_openai
        )
        bot_reply = response.choices[0].message.content
        history.append((message, bot_reply))

        # Guardar si el pedido está finalizado
        if "Los empleados le confirmarán el total" in bot_reply:
            print(f"✅ Pedido registrado: {bot_reply}")

        return history, history
    except Exception as e:
        error_msg = f"❌ Error al procesar: {str(e)}"
        history.append((message, error_msg))
        return history, history

# Interfaz en Gradio
with gr.Blocks() as demo:
    gr.Markdown("## 🍦IceBoty Heladería LIMAR")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Escribí tu pedido aquí...")
    clear = gr.Button("🗑️ Limpiar chat")

    msg.submit(chat_with_bot, [msg, chatbot], [chatbot, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

# Hugging Face ejecuta `app.py`
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
