# Areli Sarai García Medina | 20310380 | 7E

class RepresentacionDelConocimiento:

    def __init__(self):
        self.base_de_hechos = []

    def agregar_hecho(self, hecho):
        self.base_de_hechos.append(hecho)

    def verificar_hecho(self, hecho):
        return hecho in self.base_de_hechos

representacion = RepresentacionDelConocimiento()

representacion.agregar_hecho("síntoma_fiebre")
representacion.agregar_hecho("síntoma_tos")
representacion.agregar_hecho("síntoma_escalofrío")
representacion.agregar_hecho("síntoma_dolor")

sintoma = "síntoma_tos"
if representacion.verificar_hecho(sintoma):
    print(f"El síntoma '{sintoma}' está presente en la base de hechos.")
else:
    print(f"El síntoma '{sintoma}' no está presente en la base de hechos.")