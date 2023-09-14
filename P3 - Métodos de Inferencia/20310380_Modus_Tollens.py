# Areli Sarai García Medina | 20310380 | 7E

# Función para evaluar el Modus Tollens
def modus_tollens(afirmacion_condicional, observacion):
    if afirmacion_condicional and not observacion:
        return "No está lloviendo."
    else:
        return "No podemos concluir que no está lloviendo."

# Definimos las afirmaciones
afirmacion_condicional = True  # Representa "Si llueve, entonces la calle estará mojada"
observacion_calle_seca = False  # Representa "La calle no está mojada"

# Aplicamos el Modus Tollens llamando a la función
resultado = modus_tollens(afirmacion_condicional, observacion_calle_seca)

# Imprimimos la conclusión
print("Conclusión:", resultado)