print("========== CONSIGNA 1 ==========")

# Definición de los conjuntos de usuarios
A = {101, 102, 103, 104, 105, 106}  # Ejemplo: Usuarios API
B = {104, 105, 106, 107, 108}       # Ejemplo: Usuarios WEB
C = {102, 105, 109}                 # Ejemplo: Usuarios con errores

# Usuarios que usan ambas plataformas (Intersección)
ambas = A & B
print("Usuarios que usan ambas plataformas:", ambas)

# Usuarios que usan al menos una plataforma (Unión)
al_menos_una = A | B
print("Usuarios que usan al menos una plataforma:", al_menos_una)

# Usuarios que usan plataforma y no tienen errores (Diferencia)
sin_errores = (A | B) - C
print("Usuarios sin errores:", sin_errores)

# Usuarios que usan solo una plataforma (Diferencia simple)
solo_api = A - B
solo_web = B - A

print("Usuarios solo API:", solo_api)
print("Usuarios solo WEB:", solo_web)

# Usuarios en C pero no en la unión de A y B
raros = C - (A | B)
print("Usuarios en C pero no en A U B:", raros)

# Resolución usando comprensión de conjuntos (Set Comprehension)
# comp1: Guarda los elementos de A que también están en B (Equivale a la intersección A & B)
comp1 = {x for x in A if x in B}

# comp2: Guarda los elementos de la unión (A o B) que NO están en C (Equivale a sin_errores)
comp2 = {x for x in (A | B) if x not in C}

print("Comprension 1:", comp1)
print("Comprension 2:", comp2)