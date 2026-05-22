#----------- Parte E — Propiedades de la matriz -----------
M = [
 [120, 150, 100],
 [200, 180, 220],
 [90, 110, 95]
]

#M=MT
#Para que sea simétrica debe cumplirse:

#M[1][2] = M[2][1] 


#150 ≠ 200 También 100 ≠ 90

#Es decir: cuando la matriz es igual a su transpuesta.
#RTA: La matriz no es simetrica

#El determinante de la matriz es: #-194500

#Si es posible obtener la inversa, la matriz es invertible, y se puede calcular utilizando la fórmula de la matriz adjunta y el determinante.

#¿Qué implicaría que la matriz NO sea invertible?
#existe información repetida o dependiente
#algunas filas podrían obtenerse a partir de otras
#el sistema tendría datos redundantes

#----------Parte F — Análisis aplicado Función con mayor costo computacional promedio ---------------
#(120 + 150 + 100) / 3 = 123.3
#(200 + 180 + 220) / 3 = 200
#(90 + 110 + 95) / 3 = 98.3

#La función con mayor costo computacional promedio es la función 2.
#¿Qué servidor resulta más eficiente?
#(120 + 200 + 90) / 3 = 136.6
#(150 + 180 + 110) / 3 = 146.6
#(100 + 220 + 95) / 3 = 138.3
#El servidor más eficiente es el servidor 1

#--------------Recomendación técnica--------------
#Optimizar la función 2 porque presenta el mayor costo computacional.
#Redistribuir tareas hacia el servidor 1, ya que es el más eficiente.
#Revisar el rendimiento del servidor 2, debido a que posee el promedio más alto.
#plicar mejoras de código o balanceo de carga para reducir tiempos de ejecución.

#Estas decisiones permitirían:

#mejorar el rendimiento general
#disminuir demoras
#evitar sobrecarga en el sistema.
