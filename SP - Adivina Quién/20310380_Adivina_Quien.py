# Areli Sarai García Medina | 20310380 | 7E

# Adivina Quién - Animales

from tabulate import tabulate

# Inicializa la lista de animales
animales = [
    {"nombre": "León", "es_carnívoro": True, "tiene_melena": True, "vive_en_selva": True},
    {"nombre": "Elefante", "es_carnívoro": False, "tiene_melena": False, "vive_en_selva": True},
    {"nombre": "Cebra", "es_carnívoro": False, "tiene_melena": False, "vive_en_selva": True},
    {"nombre": "Pingüino", "es_carnívoro": False, "tiene_melena": False, "vive_en_selva": False},
    {"nombre": "Tortuga", "es_carnívoro": False, "tiene_melena": False, "vive_en_selva": False},
    {"nombre": "Delfín", "es_carnívoro": True, "tiene_melena": False, "vive_en_selva": False},
]

# Agrega atributos adicionales
for animal in animales:
    animal["puede_volar"] = False
    animal["es_domestico"] = False
    animal["tiene_rayas"] = False
    animal["es_acuatico"] = False
    animal["tiene_plumas"] = False


def mostrar_animales(animales):
    if not animales:
        print("No hay animales en la lista.")
        return

    atributos = list(animales[0].keys())
    headers = atributos.copy()

    tabla = []
    for animal in animales:
        fila = [animal[atributo] for atributo in atributos]
        tabla.append(fila)

    print("\nTabla de Animales:")
    print(tabulate(tabla, headers, tablefmt="grid"))

def adivinar_animal(animales):
    print("Piensa en un animal y responde las siguientes preguntas con 's' o 'n'.")
    atributos = list(animales[0].keys())

    for atributo in atributos[1:]:  # Comienza desde el segundo atributo
        if hacer_pregunta(f"¿El animal tiene {atributo}?"):
            animales = [a for a in animales if a[atributo]]
        else:
            animales = [a for a in animales if not a[atributo]]

    if len(animales) == 0:
        print("No encontré ningún animal con esos atributos.")
        print("Gracias por jugar.")
    elif len(animales) == 1:
        respuesta_correcta = hacer_pregunta(f"¿Tu animal es un {animales[0]['nombre']}? (s/n)")
        if respuesta_correcta:
            print("¡He adivinado correctamente!")
        else:
            print(f"No he adivinado correctamente. Tu animal no es un {animales[0]['nombre']}.")
            if hacer_pregunta("¿Quieres agregar un nuevo animal?"):
                agregar_nuevo_animal()
                if hacer_pregunta("¿Quieres agregar un nuevo atributo?"):
                    nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada animal: ")
                    agregar_atributo_individual(nuevo_atributo)
            else:
                print("¡Hasta luego!")
    else:
        print("No pude adivinar el animal. ¡Has ganado!")

def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Por favor, responde con 's' o 'n'.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == "s"

def agregar_nuevo_animal():
    nuevo_animal = {}
    nuevo_animal["nombre"] = input("Nombre del nuevo animal: ")

    for atributo in animales[0].keys():
        if atributo != "nombre":
            respuesta = input(f"¿El animal '{nuevo_animal['nombre']}' tiene '{atributo}'? (s/n): ").strip().lower()
            nuevo_animal[atributo] = respuesta == "s"

    animales.append(nuevo_animal)
    print(f"Se ha agregado a {nuevo_animal['nombre']} a la base de datos.")

def agregar_atributo_individual(atributo):
    for animal in animales:
        respuesta = input(f"¿El animal '{animal['nombre']}' tiene '{atributo}'? (s/n): ").strip().lower()
        if respuesta == "s":
            animal[atributo] = True
        elif respuesta == "n":
            animal[atributo] = False
        else:
            print("Respuesta no válida. Por favor, responde con 's' o 'n'.")

def jugar_de_nuevo():
    respuesta = hacer_pregunta("¿Quieres jugar de nuevo?")
    return respuesta

while True:
    mostrar_animales(animales)
    adivinar_animal(animales)
    if not jugar_de_nuevo():
        if hacer_pregunta("¿Quieres agregar un nuevo animal?"):
            agregar_nuevo_animal()
            if hacer_pregunta("¿Quieres agregar un nuevo atributo?"):
                nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada animal: ")
                agregar_atributo_individual(nuevo_atributo)
        else:
            print("¡Gracias por jugar! Hasta luego!")
            break