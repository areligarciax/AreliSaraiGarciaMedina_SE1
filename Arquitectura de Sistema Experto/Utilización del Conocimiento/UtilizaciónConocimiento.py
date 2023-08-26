# Areli Sarai García Medina | 20310380 | 7E

class UtilizacionDelConocimiento:

    def __init__(self):
        self.base_de_conocimiento = {
            "soleado": "Podrías ir a dar un paseo por el parque.",
            "nublado": "Sería un buen día para hacer ejercicio al aire libre.",
            "lluvioso": "Tal vez sea mejor quedarse en casa y ver una película."
        }

    def recomendar_actividad(self, clima):
        recomendacion = self.base_de_conocimiento.get(clima, "No tengo recomendaciones para ese clima.")
        return recomendacion

utilizacion = UtilizacionDelConocimiento()

clima_actual = input("Ingresa el clima actual (soleado/nublado/lluvioso): ")
recomendacion = utilizacion.recomendar_actividad(clima_actual)

print("Recomendación:", recomendacion)