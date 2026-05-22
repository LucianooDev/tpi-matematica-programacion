print("\nTABLA DE LA VERDAD")
valores = [True, False]
A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}
for p in valores:
    for q in valores:
        for r in valores:

            resultado = (p or q) and r

            print(p, q, r, resultado)
            

print("p q r resultado")

#Se Define usuario critico (𝑝 ∨𝑞)∧𝑟

def usuario_critico(usuario):

    p = usuario in A
    q = usuario in B
    r = usuario in C

    return (p or q) and r

#Clasificación

criticos = []
no_criticos = []

usuarios = A & B & C

for usuario in usuarios:

    if usuario_critico(usuario):
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)

print("\nUsuarios criticos:", criticos)
print("Usuarios no criticos:", no_criticos)
#-----------#Parte C — Interpretación----------
#Responder:  
#¿Qué tipo de usuario representa mayor riesgo?
# Los usuarios que representan mayor riesgo son los usuarios criticos, 102 y 105

#--------------¿Qué significa que un usuario esté en C pero no en A ∪ B?------------
#No aparece registrado con errores, ni figura utilizando api ni la web

#--------------Qué decisión tomarían como equipo programador?-------------------
#Analizar por qué los usuarios críticos generan errores.
#Optimizar el manejo de errores para futuras fallas
#analizar por que los usuarios criticos generan erorres