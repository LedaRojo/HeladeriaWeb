

# ChatBot inteligente para antención de clientes y venta de helados y complementos (detalles de la definición del proyecto y KPIs)
<img width="616" height="253" alt="image" src="https://github.com/user-attachments/assets/77dbc3c9-1b47-4c02-ba6d-feeea2b3ddfd" />


# Análisis del Mercado y Descripción de la Empresa
La empresa analizada es una cadena de heladerías, con múltiples sucursales en la ciudad de Bahía Blanca, Argentina. Fundada por tres socios, la compañía se encuentra en una fase de consolidación con la visión estratégica de expandirse a través de un modelo de franquicias. Su propuesta de valor se basa en ofrecer productos de alta calidad con una variedad de sabores que atienden tanto a consumidores individuales como a clientes corporativos.

# Transformación del Proceso de Pedidos con aplicación de IA.

Objetivo del modelo: hacer un cambio en el proceso en base al reemplazo de las llamadas telefónicas por una aplicación tipo e-commerce y la asistencia vía whatsapp para tomar pedidos mediante un chatbot con IA.

# A. Migración de pedidos telefónicos a una app de pedidos tipo e-commerce
En lugar de atender llamadas manualmente, se implementará una app móvil y web donde los clientes puedan hacer pedidos de manera rápida e intuitiva.
Flujo del nuevo proceso en la app:
●	Registro/Login: El cliente inicia sesión con su correo o alguna red social.
●	Selección de productos
●	Personalización del pedido: Opción de agregar notas, elegir salsas, combos, etc.
●	Confirmación y pago: Se muestran los métodos de pago y se valida la transacción.
●	Envío a cocina: Solo se confirma la orden si el pago es exitoso.
●	Seguimiento en tiempo real: El cliente recibe actualizaciones del estado de su pedido.
# B. Implementación de un Chatbot con IA en WhatsApp
En lugar de atender los pedidos manualmente por WhatsApp, se integrará un chatbot con Procesamiento de Lenguaje Natural (NLP) que interactúe con los clientes de manera natural y automatizada.

# Detalles técnicos:

# 1. Entrenamiento del chatbot
# A. Definir las intenciones y entidades
     Delimitar tipos de mensajes que puede recibir el bot:	
# ●	Intenciones (lo que el usuario quiere lograr):

1.      hacer un pedido
2.      consultar sabores
3.      preguntar precios  
4.      consultar horarios
5.      consultar aspectos del delivery y solicitarlo
6.      consultar promociones
7.      consultar Toppings
8.      consultar formas de pago, etc.
 
# ●	Entidades   (los detalles que acompañan esa intención):
1.      sabores de helado: chocolate, vainilla, frutilla, dulce de leche, etc.
2.      Delivery hoy a la noche
3.      Sin toopings, etc

 
# B. Entrenamiento del modelo
Se usará una plataforma de NLP (Procesamiento de Lenguaje Natural) a   seleccionar entre las siguientes :
●	Rasa (open source, muy bueno para personalizar)
●	Dialogflow (de Google)
●	Botpress
●	Wit.ai (de Meta)
# 1. Se cargarán ejemplos de frases por intención:
Intención: consultar sabores
- ¿Qué sabores de helados tienen?
      - ¿Tienen helado de pistacho?
- ¿Qué variedades hay hoy?
Y  el bot aprenderá a reconocer la intención con lenguaje natural.
 
# 2. Capacidad de Responder consultas raras
Se definirá una política de fallback (respuesta por defecto), por ejemplo:
“¡No entendí eso! ¿Querés que te pase los sabores disponibles o nuestras promos?”
●	Se entrenará el chat con ejemplos raros o fuera de contexto. Cuanto más lo entrenemos con casos reales, mejor va a saber manejarse.
●	Se le agregará lógica para derivar a un humano si el bot se bloquea varias veces:
“Parece que no puedo ayudarte con eso. ¿Querés que te contacte una persona del equipo?”
 
# 3. Actualización (sabores nuevos, precios, etc.)
Se usará una Conexión a una base de datos o archivo dinámico
Específicamente, el bot consulta esa base en tiempo real, así no necesitará reentrenamiento.


# 4. Conexión con WhatsApp
WhatsApp no permite bots directamente, pero se usará una de las siguientes  opciones:
●	Twilio (con API oficial de WhatsApp)
●	360Dialog (se integra con plataformas como Dialogflow o Rasa)
●	Zoko, Wati, Landbot, etc. (más visuales, ideales para pequeños negocios)

 El chatBot tendrá la capacidad de interactuar en lenguaje natural (humano) con los clientes ya que estará conectado con un modelo de la Api de OpenAI.
También, se le agregará un módulo simple para que pueda aprender de las interacciones, guardando logs de preguntas que el bot no pudo responder para usarlos en seguir mejorando el entrenamiento.
 
Flujo del nuevo proceso en WhatsApp:
●	El cliente escribe al WhatsApp de la empresa.
●	El chatbot IA responde con un saludo amigable y guía el pedido.
●	El cliente elige su pedido con mensajes tipo “Quiero1 kilo de helado”.
●	El bot confirma el pedido y envía el link de pago.
●	Validación del pago antes de enviar el pedido a cocina.
●	Confirmación y tiempo estimado de entrega.

Es importante para ambos procesos tener la validación del Pago antes de Enviar a preparación de pedidos: Tanto en la app como en WhatsApp, se integrará una validación de pago antes de confirmar el pedido.
Proceso de validación de pago:
●	El cliente elige su método de pago.
●	El sistema verifica que la transacción se realizó con éxito.
●	Si es exitosa, se envía el pedido a "preparación de pedidos" automáticamente.
●	Si falla, se notifica al cliente y se solicita otro método de pago.


## Beneficios del Nuevo Proceso Digitalizado
# 1. Reducción del tiempo de atención y optimización operativa.
●	Eliminando la gestión manual de llamadas y mensajes de WhatsApp, los tiempos de atención bajarán drásticamente:
  		- Pedidos telefónicos: De 3-5 minutos a 0 minutos (eliminado).
  		- Pedidos por WhatsApp: De 2-4 minutos a 30-60 segundos con IA.
- Pedidos por App: cambia el pedido telefonico de 3-5 minutos a Menos de 1 minuto con opciones rápidas y guardado de pedidos frecuentes.

●	Impacto directo: Mayor eficiencia operativa, permitiendo procesar más pedidos en menos tiempo.
# 2. Incremento de clientes por practicidad y rapidez en los pedidos.
●	Facilitar el pedido mediante una app intuitiva y un chatbot reduce la fricción del proceso.
●	Los clientes podrán pedir en segundos sin esperas, aumentando la fidelización y frecuencia de compra.
●	Expectativa de crecimiento: Un incremento del 15-30% en la tasa de conversión de pedidos en los primeros meses.
# 3. Mejora en la experiencia del usuario.
●	Autoatención 24/7: Ya no dependerá del horario o disponibilidad del personal.
●	Personalización: La app y el chatbot pueden recordar pedidos previos y sugerir opciones.
●	Fluidez: Los clientes no perderán tiempo explicando su pedido cada vez que llaman.
●	Estado en tiempo real: Notificaciones automáticas sobre el estado del pedido.
●	Medios de pago ágiles: Eliminación del pago en efectivo con validaciones seguras.
# 4. Disminución en la carga operativa y errores en la toma de pedidos.
●	Pedidos digitales = 0 errores humanos en la interpretación de órdenes.
●	Menos carga para empleados, permitiéndoles enfocarse en la producción y entrega.
●	Reducción del 80-90% en consultas sobre el estado de pedidos, ya que los clientes podrán verlo en la app.
# 5. Disminución de quejas y reclamos por pedidos erróneos.
●	Al ser el cliente quien elige, revisa y confirma su pedido, se eliminan malentendidos.
●	Impacto esperado: Disminución del 60-80% de reclamos relacionados con errores en pedidos.
# KPIs Beneficiados:
Con la optimización vemos que varios Kpi´s se ven afectados en el proceso de la empresa.

<img width="796" height="344" alt="image" src="https://github.com/user-attachments/assets/1c26e34f-1c35-4d4c-a608-bf55d64cc68e" />


# Costos
<img width="865" height="280" alt="image" src="https://github.com/user-attachments/assets/3088d41b-7899-4eea-8db5-b81ad5de91ad" />


