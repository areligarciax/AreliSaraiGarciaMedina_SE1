# Areli Sarai García Medina | 20310380 | 7E

# Clue - EL robo del Diamante

import random

# Define los personajes, locaciones y herramientas
personajes = ["Juan", "Maria", "Carlos", "Lupita", "Rafael"]
locaciones = ["Mansión Blackwood", "Banco Central", "Museo de Arte", "Estación de Metro", "Cafetería Acogedora"]
herramientas = ["Kit de Ladrón Profesional", "Caja Fuerte Portátil", "Rayo Desintegrador", "Gato Distraído", "Pluma Grabadora"]


# Genera una solución aleatoria
def Aleatorio():
    solucion = {
        "personaje": random.choice(personajes),
        "locacion": random.choice(locaciones),
        "herramienta": random.choice(herramientas)
    }
    return solucion


def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Por favor, responde con 's' o 'n'.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == "s"


def jugar_de_nuevo():
    respuesta = hacer_pregunta("¿Quieres jugar de nuevo?")
    return respuesta


def jugar():
    intentos = 0
    solucion = Aleatorio()
    while True:
        intentos += 1

        # Coartadas de Juan
        if solucion['personaje'] == "Juan":
            texto = '''
                Juan, un conocido ladrón de diamantes, ha perpetrado su último golpe en la lujosa Mansión Blackwood.
                Después de robar un valioso diamante, se escondió en algún lugar de la mansión. La policía lo rodea y está interrogando a los sospechosos.
                Cada uno de ellos ofrece su coartada:

                - Juan afirma que estaba en el jardín de la mansión, revisando el diamante que acaba de robar.
                - María dijo que estaba en el Banco Central, manejando una transferencia financiera de alto nivel.
                - Carlos mencionó que estaba en el Museo de Arte, analizando una pintura valiosa.
                - Lupita alegó que estaba en la Estación de Metro, buscando su teléfono móvil perdido.
                - Rafael declaró que estaba en la Cafetería Acogedora, disfrutando de un café con un conocido diplomático extranjero.
                '''
            print(texto)
            suposicion_ladron = input(
                "\n-----¿Quién es el ladrón?-----\na)Juan \nb)María \nc)Carlos \nd)Lupita \ne)Rafael\n")
            suposicion_locacion = input(
                "\n¿Dónde escondió el diamante?:\na)Mansión Blackwood \nb)Banco Central \nc)Museo de Arte \nd)Estación de Metro \ne)Cafetería Acogedora\n")
            suposicion_herramienta = input(
                "\n¿Con qué herramienta escondió el diamante?:\na)Kit de Ladrón Profesional \nb)Caja Fuerte Portátil \nc)Rayo Desintegrador \nd)Gato Distraído \ne)Pluma Grabadora\n")
            if suposicion_ladron == 'a' and suposicion_locacion == 'a' and suposicion_herramienta == 'd':
                texto = '''
                    ¡Felicidades, has atrapado a Juan, el ladrón de diamantes!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto.
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")

        # Coartadas de María
        if solucion['personaje'] == "Maria":
            texto = '''
                María, una respetable ciudadana, se encontraba realizando una transacción bancaria en el Banco Central de la ciudad.
                Mientras tanto, un diamante fue robado y escondido en un lugar secreto. La policía está interrogando a los sospechosos.
                Cada uno de ellos ofrece su coartada:

                - Juan afirma que estaba en el jardín de la mansión, revisando el diamante que acaba de robar.
                - María dijo que estaba en el Banco Central, manejando una transferencia financiera de alto nivel. Además, tiene un testigo que puede confirmar su coartada.
                - Carlos mencionó que estaba en el Museo de Arte, analizando una pintura valiosa.
                - Lupita alegó que estaba en la Estación de Metro, buscando su teléfono móvil perdido.
                - Rafael declaró que estaba en la Cafetería Acogedora, disfrutando de un café con un conocido diplomático extranjero.
                '''
            print(texto)
            suposicion_ladron = input(
                "\n-----¿Quién es el ladrón?-----\na)Juan \nb)María \nc)Carlos \nd)Lupita \ne)Rafael\n")
            suposicion_locacion = input(
                "\n¿Dónde escondió el diamante?:\na)Mansión Blackwood \nb)Banco Central \nc)Museo de Arte \nd)Estación de Metro \ne)Cafetería Acogedora\n")
            suposicion_herramienta = input(
                "\n¿Con qué herramienta escondió el diamante?:\na)Kit de Ladrón Profesional \nb)Caja Fuerte Portátil \nc)Rayo Desintegrador \nd)Gato Distraído \ne)Pluma Grabadora\n")
            if suposicion_ladron == 'b' and suposicion_locacion == 'b' and suposicion_herramienta == 'c':
                texto = '''
                    ¡Felicidades, has atrapado a María, la ladrona de diamantes!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto.
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")

        # Coartadas de Carlos
        if solucion['personaje'] == "Carlos":
            texto = '''
                Carlos, un amante del arte, se encontraba en el Museo de Arte de la ciudad, analizando una pintura valiosa.
                En medio de su visita, un diamante fue robado y escondido en un lugar secreto. La policía está interrogando a los sospechosos.
                Cada uno de ellos ofrece su coartada:

                - Juan afirma que estaba en el jardín de la mansión, revisando el diamante que acaba de robar.
                - María dijo que estaba en el Banco Central, manejando una transferencia financiera de alto nivel.
                - Carlos mencionó que estaba en el Museo de Arte, analizando una pintura valiosa. Tiene una grabación de seguridad que lo respalda.
                - Lupita alegó que estaba en la Estación de Metro, buscando su teléfono móvil perdido.
                - Rafael declaró que estaba en la Cafetería Acogedora, disfrutando de un café con un conocido diplomático extranjero.
                '''
            print(texto)
            suposicion_ladron = input(
                "\n-----¿Quién es el ladrón?-----\na)Juan \nb)María \nc)Carlos \nd)Lupita \ne)Rafael\n")
            suposicion_locacion = input(
                "\n¿Dónde escondió el diamante?:\na)Mansión Blackwood \nb)Banco Central \nc)Museo de Arte \nd)Estación de Metro \ne)Cafetería Acogedora\n")
            suposicion_herramienta = input(
                "\n¿Con qué herramienta escondió el diamante?:\na)Kit de Ladrón Profesional \nb)Caja Fuerte Portátil \nc)Rayo Desintegrador \nd)Gato Distraído \ne)Pluma Grabadora\n")
            if suposicion_ladron == 'c' and suposicion_locacion == 'c' and suposicion_herramienta == 'b':
                texto = '''
                    ¡Felicidades, has atrapado a Carlos, el ladrón de diamantes!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto.
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")

        # Coartadas de Lupita
        if solucion['personaje'] == "Lupita":
            texto = '''
                Lupita, una ciudadana en busca de su teléfono móvil perdido, se aventuró al subterráneo de la ciudad en su búsqueda.
                Mientras tanto, un diamante fue robado y escondido en un lugar secreto. La policía está interrogando a los sospechosos.
                Cada uno de ellos ofrece su coartada:

                - Juan afirma que estaba en el jardín de la mansión, revisando el diamante que acaba de robar.
                - María dijo que estaba en el Banco Central, manejando una transferencia financiera de alto nivel.
                - Carlos mencionó que estaba en el Museo de Arte, analizando una pintura valiosa.
                - Lupita alegó que estaba en la Estación de Metro, buscando su teléfono móvil perdido. Varias personas pueden confirmar su presencia.
                - Rafael declaró que estaba en la Cafetería Acogedora, disfrutando de un café con un conocido diplomático extranjero.
                '''
            print(texto)
            suposicion_ladron = input(
                "\n-----¿Quién es el ladrón?-----\na)Juan \nb)María \nc)Carlos \nd)Lupita \ne)Rafael\n")
            suposicion_locacion = input(
                "\n¿Dónde escondió el diamante?:\na)Mansión Blackwood \nb)Banco Central \nc)Museo de Arte \nd)Estación de Metro \ne)Cafetería Acogedora\n")
            suposicion_herramienta = input(
                "\n¿Con qué herramienta escondió el diamante?:\na)Kit de Ladrón Profesional \nb)Caja Fuerte Portátil \nc)Rayo Desintegrador \nd)Gato Distraído \ne)Pluma Grabadora\n")
            if suposicion_ladron == 'd' and suposicion_locacion == 'd' and suposicion_herramienta == 'a':
                texto = '''
                    ¡Felicidades, has atrapado a Lupita, la ladrona de diamantes!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, eso es incorrecto.
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")

        # Coartadas de Rafael
        if solucion['personaje'] == "Rafael":
            texto = '''
                Rafael, un amante del café, estaba en la Cafetería Acogedora de la ciudad disfrutando de su bebida favorita.
                Mientras tanto, un diamante fue robado y escondido en un lugar secreto. La policía está interrogando a los sospechosos.
                Cada uno de ellos ofrece su coartada:

                - Juan afirma que estaba en el jardín de la mansión, revisando el diamante que acaba de robar.
                - María dijo que estaba en el Banco Central, manejando una transferencia financiera de alto nivel.
                - Carlos mencionó que estaba en el Museo de Arte, analizando una pintura valiosa.
                - Lupita alegó que estaba en la Estación de Metro, buscando su teléfono móvil perdido.
                - Rafael declaró que estaba en la Cafetería Acogedora, disfrutando de un café con un conocido diplomático extranjero. Además, hay una foto de su encuentro.
                '''
            print(texto)
            suposicion_ladron = input(
                "\n-----¿Quién es el ladrón?-----\na)Juan \nb)María \nc)Carlos \nd)Lupita \ne)Rafael\n")
            suposicion_locacion = input(
                "\n¿Dónde escondió el diamante?:\na)Mansión Blackwood \nb)Banco Central \nc)Museo de Arte \nd)Estación de Metro \ne)Cafetería Acogedora\n")
            suposicion_herramienta = input(
                "\n¿Con qué herramienta escondió el diamante?:\na)Kit de Ladrón Profesional \nb)Caja Fuerte Portátil \nc)Rayo Desintegrador \nd)Gato Distraído \ne)Pluma Grabadora\n")
            if suposicion_ladron == 'e' and suposicion_locacion == 'e' and suposicion_herramienta == 'e':
                texto = '''
                    ¡Felicidades, has atrapado a Rafael, el ladrón de diamantes!
                    '''
                print(texto)
                break
            else:
                texto = '''
                    Lo lamento, esa respuesta NO es correcta.
                    '''
                print(texto)
                print("Llevas " + str(intentos) + " intentos.\n")


if __name__ == "__main__":
    print("Bienvenido a CLUE - El Robo del Diamante.")
    while True:
        jugar()
        if not jugar_de_nuevo():
            print("¡Gracias por jugar! -Hasta luego-")
            break