# Areli Sarai García Medina | 20310380 | 7E

class AdquisicionDeConocimiento:

    def __init__(self):
        self.conocimiento = {}

    def capturar_informacion(self):
        print("Bienvenido al sistema experto de recomendación de actividades al aire libre.")
        temperatura = float(input("Ingresa la temperatura actual en grados Celsius: "))
        clima = input("¿Está soleado, nublado o lluvioso?: ")

        self.conocimiento['temperatura'] = temperatura
        self.conocimiento['clima'] = clima

    def generar_recomendacion(self):
        temperatura = self.conocimiento.get('temperatura', 0)
        clima = self.conocimiento.get('clima', '')

        if temperatura >= 25 and clima == 'soleado':
            return "Podrías ir a la playa a disfrutar del sol."
        elif temperatura >= 15 and clima == 'nublado':
            return "Sería agradable dar un paseo por el parque."
        elif temperatura >= 10 and clima == 'lluvioso':
            return "Podrías quedarte en casa y leer un libro."
        else:
            return "Tal vez sea mejor quedarse en casa hoy."

adquisicion = AdquisicionDeConocimiento()
adquisicion.capturar_informacion()
recomendacion = adquisicion.generar_recomendacion()

print(recomendacion)