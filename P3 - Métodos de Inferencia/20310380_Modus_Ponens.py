# Areli Sarai García Medina | 20310380 | 7E

# Función para evaluar el Modus Ponens
def modus_ponens(afirmacion_condicional, afirmacion_antecedente):
    if afirmacion_condicional and afirmacion_antecedente:
        return "La alarma se activará."
    else:
        return "No podemos concluir si la alarma se activará o no."

# Definimos las afirmaciones
afirmacion_condicional = True  # Representa "Si el sensor de movimiento detecta intrusos, la alarma se activará"
afirmacion_antecedente = True  # Representa "El sensor de movimiento detecta intrusos"

# Aplicamos el Modus Ponens llamando a la función
resultado = modus_ponens(afirmacion_condicional, afirmacion_antecedente)

# Imprimimos la conclusión
print("Conclusión:", resultado)