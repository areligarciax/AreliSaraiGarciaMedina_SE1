# Areli Sarai García Medina | 20310380 | 7E

# Lista con preguntas y respuestas iniciales
conocimiento = [
    {"pregunta": "Hola", "respuesta": "¡Hola! Estoy aquí para ayudarte."},
    {"pregunta": "Cómo estás", "respuesta": "Estoy bien, gracias. ¿Cómo puedo ayudarte hoy?"},
    {"pregunta": "De qué te gustaría hablar", "respuesta": "Puedo hablar de muchas cosas. ¿Tienes alguna pregunta en particular?"},
    {"pregunta": "Cuál es tu nombre", "respuesta": "No tengo un nombre en particular, me puedes llamar Bot."},
    {"pregunta": "Cuál es el clima para hoy", "respuesta": "Lo siento, no puedo proporcionar información sobre el clima en este momento."},
    {"pregunta": "Cuál es el sentido de la vida", "respuesta": "El sentido de la vida es un tema filosófico profundo y subjetivo. Algunas personas creen que es buscar la felicidad, mientras que otras tienen sus propias interpretaciones."},
    {"pregunta": "Cuál es la capital de España", "respuesta": "La capital de España es Madrid."},
    {"pregunta": "Cuál es la capital de Italia", "respuesta": "La capital de Italia es Roma."},
    {"pregunta": "Cómo se hace una pizza",
     "respuesta": "Para hacer una pizza, necesitas masa, salsa de tomate, queso y tus ingredientes favoritos. Estira la masa, agrega salsa de tomate, queso y tus ingredientes, luego hornea hasta que esté dorada."},
    {"pregunta": "Cuál es la fórmula del agua",
     "respuesta": "La fórmula química del agua es H2O, lo que significa que está compuesta por dos átomos de hidrógeno y un átomo de oxígeno."},
    {"pregunta": "Cuántos planetas hay en el sistema solar",
     "respuesta": "Hay ocho planetas en el sistema solar: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano y Neptuno."}
]

def chat():
    print("¡Bienvenido al chat!")

    while True:
        mensaje = input("Tú: ").lower()
        if mensaje == "adiós" or mensaje == "chao" or mensaje == "hasta luego":
            print("Bot: ¡Adiós! Hasta la próxima.")
            break
        respuesta = buscar_respuesta(mensaje)
        if respuesta:
            print(f"Bot: {respuesta}")
        else:
            print("Bot: Lo siento, no tengo una respuesta para eso.")
            agregar_conocimiento(mensaje)

def buscar_respuesta(mensaje):
    for conocimiento_item in conocimiento:
        if conocimiento_item["pregunta"].lower() == mensaje:
            return conocimiento_item["respuesta"]
    return None

def agregar_conocimiento(pregunta):
    respuesta = input("Bot: No sé la respuesta. ¿Puedes proporcionar una respuesta? ")
    conocimiento.append({"pregunta": pregunta, "respuesta": respuesta})
    print("Bot: Gracias por compartir tu conocimiento.\n")

if __name__ == "__main__":
    chat()