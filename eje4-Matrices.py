print("\n========== MATRICES ==========")

M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
    #Fila 1 = autenticación de usuarios
    #Fila 2 = procesamiento de datos
    #Fila 3 = generación de reportes
]

C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
    ]               
    #Columna 1 = Servidor A
    #Columna 2 = Servidor B
    #Columna 3 = Servidor C

#¿Que representa un valor cualquiera de la matriz?
#Cada número representa el tiempo promedio de ejecución de una función en un servidor específico.
#120 Tarda 120 Milisegundos, Función 1 y se ejecuta en el servidor 1

#La matriz M es 3 x 3, Por que tiene 3 filas y 3 columnas 
#La Matriz C Es lo mismo , y es posible hacer M * C
#la cantidad de columnas de la primera matriz es igual a la cantidad de filas de la segunda matriz
#El tamaño de la matriz tendra 3 x 3, Se conservan Las filas de M y columnas de C


print("\nPromedio por funcion")

for i in range(3):

    promedio = sum(M[i]) / 3

    print("Funcion", i + 1, ":", promedio)

# Promedio por servidor

print("\nPromedio por servidor")

for j in range(3):

    suma = 0

    for i in range(3):

        suma += M[i][j]

    promedio = suma / 3

    print("Servidor", j + 1, ":", promedio)

    # Transpuesta
print("\nMatriz transpuesta")

MAT = []

for j in range(3):

    fila = []

    for i in range(3):

        fila.append(M[i][j])

    MAT.append(fila)

for fila in MAT:
    print(fila)
    #-----ahora las filas representan los servidores y las columnas representan las funciones.-----

    # Producto matricial T = M * C
print("\nProducto matricial")

T = []

for i in range(3):

    fila = []

    for j in range(3):

        suma = 0

        for k in range(3):

            suma += M[i][k] * C[k][j]

        fila.append(suma)

    T.append(fila)

for fila in T:
    print(fila)
#----------¿Qué podría representar cada valor de la matriz T?-------------

#Cada valor podría representar una combinación entre:

#tiempo de ejecución y cantidad de ejecuciones
#---------¿Tiene sentido físico o práctico esta operación?-----------------
#En caso de considerar que el producto no representa correctamente una magnitud útil:  

#-----o Explicar por qué o Proponer una alternativa más adecuada para combinar la información de tiempo y cantidad de ejecuciones (por ejemplo: otra operación o enfoque----
#Los tiempos promedio y las cantidades de ejecuciones representan cosas distintas.
#al multiplicarlas mediante producto matricial se pierde una interpretación directa.

#Alternativa más adecuada: multiplicar cada tiempo por su cantidad de ejecuciones correspondiente.





