print("========== CONSIGNA 1 ==========")

A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

# Usuarios que usan ambas plataformas
ambas = A & B
print("Usuarios que usan ambas plataformas:", ambas)

# Usuarios que usan al menos una plataforma
al_menos_una = A | B
print("Usuarios que usan al menos una plataforma:", al_menos_una)

# Usuarios que usan plataforma y no tienen errores
sin_errores = (A | B) - C
print("Usuarios sin errores:", sin_errores)

# Usuarios que usan solo una plataforma
solo_api = A - B
solo_web = B - A

print("Usuarios solo API:", solo_api)
print("Usuarios solo WEB:", solo_web)

# Usuarios en C pero no en A U B
raros = C - (A | B)
print("Usuarios en C pero no en A U B:", raros)

comp1 = {x for x in A if x in B}
comp2 = {x for x in (A | B) if x not in C}

print("Comprension 1:", comp1)
print("Comprension 2:", comp2)
