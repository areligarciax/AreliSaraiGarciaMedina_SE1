# Areli Sarai García Medina | 20310380 | 7E

class TratamientoDelConocimiento:

    def __init__(self):
        self.base_de_conocimiento = []

    def agregar_regla(self, condiciones, recomendacion):
        self.base_de_conocimiento.append({"condiciones": condiciones, "recomendacion": recomendacion})

    def generar_recomendacion(self, caracteristicas):
        for regla in self.base_de_conocimiento:
            if all(cond in caracteristicas for cond in regla["condiciones"]):
                return regla["recomendacion"]
        return "No se pudo generar una recomendación."

tratamiento = TratamientoDelConocimiento()

tratamiento.agregar_regla(["precio_bajo", "buena_calidad"], "Te recomendamos el producto A.")
tratamiento.agregar_regla(["precio_moderado", "alto_desempeno"], "Te recomendamos el producto B.")
tratamiento.agregar_regla(["alta_calidad", "caracteristicas_avanzadas"], "Te recomendamos el producto C.")

caracteristicas_usuario = ["precio_moderado", "alto_desempeno"]
recomendacion = tratamiento.generar_recomendacion(caracteristicas_usuario)

print("Basado en las características, la recomendación es:", recomendacion)