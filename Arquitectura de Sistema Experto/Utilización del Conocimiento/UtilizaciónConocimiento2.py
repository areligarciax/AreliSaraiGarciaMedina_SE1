# Areli Sarai García Medina | 20310380 | 7E

class UtilizacionDelConocimiento:

    def __init__(self):
        self.base_de_conocimiento = {
            "cactus": {
                "salud_buena": "Riega el cactus ligeramente cada dos semanas.",
                "salud_mala": "Deja de regar el cactus hasta que la tierra esté seca."
            },
            "orquídea": {
                "salud_buena": "Riega la orquídea con cuidado una vez por semana.",
                "salud_mala": "Corta las hojas enfermas y repota la orquídea en tierra fresca."
            },
            "suculenta": {
                "salud_buena": "Riega la suculenta con moderación cada 10 días.",
                "salud_mala": "Trasplanta la suculenta en una maceta más grande y colócala en un lugar soleado."
            }
        }

    def dar_consejo(self, tipo_planta, estado_salud):
        consejo = self.base_de_conocimiento.get(tipo_planta, {}).get(estado_salud, "No tengo consejos para esa combinación.")
        return consejo

utilizacion = UtilizacionDelConocimiento()

tipo_planta = input("Ingresa el tipo de planta (cactus/orquídea/suculenta): ")
estado_salud = input("Ingresa el estado de salud (salud_buena/salud_mala): ")

consejo = utilizacion.dar_consejo(tipo_planta, estado_salud)

print("Consejo:", consejo)