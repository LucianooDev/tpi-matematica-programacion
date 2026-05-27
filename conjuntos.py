#CONSIGNA TEORÍA DE CONJUNTOS: validación de usuarios y análisis de consistencia del sistema.
#Una empresa de desarrollo analiza el comportamiento de usuarios de su plataforma.
#Se cuenta con registros de IDs de usuarios según distintas actividades.

print("========== CONSIGNA 1 ==========")

#-----------------------------
# Definimos conjuntos (set) de usuarios
A = {101, 102, 103, 104, 105, 106}  #API
B = {104, 105, 106, 107, 108}       #WEB
C = {102, 105, 109}                 #con errores

# Usuarios que usan ambas plataformas (Intersección)
ambas = A & B
#elementos que están en A y B al mismo tiempo
print("Usuarios que usan ambas plataformas:", ambas)

# Usuarios que usan al menos una plataforma (Unión)
al_menos_una = A | B
#une elementos de A y B sin repetir
print("Usuarios que usan al menos una plataforma:", al_menos_una)

# Usuarios que usan plataforma sin errores (Diferencia)
sin_errores = (A | B) - C
#unimos usuarios activos y eliminamos usuarios con errores 
print("Usuarios sin errores:", sin_errores)

# Usuarios que usan solo una plataforma (Diferencia simple)
solo_api = A - B
solo_web = B - A
#elementos que están en un conjunto pero no en otro

print("Usuarios solo API:", solo_api)
print("Usuarios solo WEB:", solo_web)

# Usuarios en C pero no en la unión de A y B
raros = C - (A | B)   #a usuarios con errores aplicamos diferencia para eliminar usuarios que usan plataformas
print("Usuarios en C pero no en A U B:", raros)
#----------------------------

#----------------------------
# COMPRENSIÓN DE CONJUNTOS (RESOLUCIÓN)

#Intersección A & B (crea un conjunto con los elementos de A, pero solo si existen en B)
comp1 = {x for x in A if x in B}
#Recorre A (x) y filtra los que también están en B

#Diferencia (equivale a sin_errores)
comp2 = {x for x in (A | B) if x not in C}
#Recorre unión A y B y guarda elementos que no están en C

print("Comprension 1:", comp1)
print("Comprension 2:", comp2)
#----------------------------

#----------------------------
# FUNCIÓN LÓGICA
#(p:A) (q:B) (r:C)
def usuario_critico(p, q, r):
    return (p or q) and r
#función con 3 parámetros que: devuelve true si el usuario está en A o B, y también está en C
#---------------------------

#-----------------------------
#TABLA DE VERDAD
print("\nTABLA DE VERDAD")

valores = [True, False]

for p in valores:
    for q in valores:
        for r in valores:

            resultado = usuario_critico(p, q, r)

            print(p, q, r, resultado)


# CLASIFICACION DE USUARIOS
print("\nCLASIFICACION DE USUARIOS")

todos = A | B | C

for usuario in todos:

    p = usuario in A
    q = usuario in B
    r = usuario in C

    if usuario_critico(p, q, r):
        print(usuario, "-> CRITICO")

    else:
        print(usuario, "-> NO CRITICO")