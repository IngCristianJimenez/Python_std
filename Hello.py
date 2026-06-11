print ('Hello World')

#Este es un comentario de una sola línea

"""
Este es un comentario
de varias líneas
"""

#Python distingue entre máyusculas y minúsculas

Variable = 1
variable = 2
VARIABLE = 3

""" Todas las variables anteriores 
son diferentes"""

"""
A diferencia de otros lenguajes. Python no requiere el uso de punto y coma (;)
al final de cada instrucción. Sin embargo si se desea escribir varias instrucciones
en una sola línea, se pueden separar con punto y coma.
"""

#Por ejemplo:

# instruccion1; instruccion2; instruccion3


#Uso de paréntesis

"""
Los paréntesis se utilizan para agrupar expresiones, definir funciones y realizar llamadas a funciones.
"""
#Por ejemplo:

# resultado = (a + b) * c


#Tipos de datos básicos

Enteros = int

#Ejemplos:

edad = 25
cantidad = 100

Flotantes = float   # aquellos que tienen una parte decimal

precio = 9.99
altura = 1.75


# Cadenas_de_texto = strings

"""
Secuencias de caracteres encerradas entre comillas simples ('...') o dobles ("...").
Se utilizan para representar texto en Python.
"""

nombre = "Juan"
mensaje = '¡Hola Mundo!'


# Puedes incluir caracteres especiales en las cadenas utilizando el carácter de escape \.
# Por ejemplo, para incluir comillas dentro de una cadena, puedes usar \' o \". 
# También puedes utilizar la notación de triple comilla ('''...''' o """...""") 
# para crear cadenas de varias líneas.


#Booleanos

"""
Representan los valores de verdad: True (verdadero) y False (falso).
"""

es_mayor_de_edad = True
tiene_descuento = False

# Nota
# Los valores booleanos en Python comienzan con una letra mayúscula: True y False.


# Declaración y asignación de variables

"""
Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas.
"""

nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

# También puedes asignar el mismo valor a múltiples variables en una sola línea utilizando el operador de asignación múltiple:

a = b = c = 10

"""
*** Los nombres de las variables solo pueden contener letras (a-z, A-Z), números (0-9) y guiones bajos (_). No pueden comenzar con un número.

*** Python distingue entre mayúsculas y minúsculas, por lo que nombre y Nombre son variables diferentes.

*** No se pueden utilizar palabras clave reservadas de Python como nombres de variables (por ejemplo, if, else, for, while, etc.).
"""


# Aritméticos

"""

* Suma (+): suma dos valores.
* Resta (-): resta el segundo valor del primero.
* Multiplicación (*): multiplica dos valores.
* División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
* División entera (//): divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
* Módulo (%): devuelve el resto de la división entre el primer valor y el segundo.
* Exponenciación (**): eleva el primer valor a la potencia del segundo.

"""

#    Ejemplos:
    
#    a = 10
#    b = 3

#    suma = a + b   # 13
#    resta = a - b    # 7
#    multiplicacion = a * b    # 30
#    division = a / b   # 3.333333333
#    división_entera = a // b   # 3
#    modulo = a % b   # 1
#    exponenciacion = a ** b   # 1000


""" 
De comparación

Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False)
según el resultado de la comparación.

"""

# Los operadores de comparación en Python son:
# 
# Igual a (==): devuelve True si ambos valores son iguales.
# Diferente de (!=): devuelve True si los valores son diferentes.
# Mayor que (>): devuelve True si el primer valor es mayor que el segundo.
# Menor que (<): devuelve True si el primer valor es menor que el segundo.
# Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo.
# Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo.


# Ejemplos:

# a = 10
# b = 3

# igual = a == b   # False
# diferente = a != b   # True
# mayor que = a > b   # True
# menor que = a < b   # False
# mayor o igual = a >= b   # True
# menor o igual = a <= b   # False


"""
Lógicos

Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones.

"""

# Los operadores lógicos en Python son:

# AND (and): devuelve True si ambas condiciones son verdaderas.
# OR (or): devuelve True si al menos una de las condiciones es verdadera.
# NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.

"""
Ejemplo:

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

"""


# Estructuras condicionales

""" 
Nos permiten ejecutar diferentes bloques de código según se cumpla o no una determinada condición.
En Python, las estructuras condicionales más utilizadas son if, if-else y if-elif-else.
"""

# IF

"""
Se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:

if condicion:

   # Bloque de código a ejecutar si la condición es verdadera
   instrucciones

"""

# Ejemplo:

edad = 18

if edad >= 18:
   print ("Eres mayor de edad.")


"""
En este ejemplo, si la variable edad es mayor o igual a 18,
se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad."
"""

# IF-ELSE

"""
nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa. La sintaxis básica es la siguiente:

edad = 15


if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")


   En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje 
   "Eres mayor de edad." De lo contrario, se ejecutará el bloque de código dentro del else y se imprimirá el mensaje "Eres menor de edad."
"""


# IF-ELIF-ELSE

# La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos.

"""
La sintaxis básica es la siguiente:

if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones

"""


# Ejemplo:
# 
# calificacion = 85
# 
# 
# if calificacion >= 90:
#    print ("Excelente")
# 
# elif calificacion >= 80:
#    print ("Muy bueno")
# 
# elif calificacion >= 70:
#    print ("Bueno")
# 
# else:
#    print ("Necesita mejorar")


"""
En este ejemplo, se evalúan múltiples condiciones en orden. 
- Si la variable calificación es mayor o igual a 90, se imprime "Excelente".
- Si no se cumple la primera condición, pero calificación es mayor o igual a 80, se imprime "Muy bueno".
- Si no se cumplen las condiciones anteriores, pero calificación es mayor o igual a 70, se imprime "Bueno".
- Si ninguna de las condiciones anteriores es verdadera, se ejecuta el bloque else y se imprime "Necesita mejorar".
"""


Bucles = "loops"

# Los bucles nos permiten repetir un bloque de código varias veces. En Python, los bucles más comunes son for y while.


# For

"""

Se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. 
"""

# La sintaxis básica es la siguiente:

# for variable in secuencia:
# 
#     # Bloque de código a repetir
#     instrucciones

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)

"""
En este ejemplo, el bucle for itera sobre la lista frutas.
En cada iteración, la variable fruta toma el valor de un elemento de la lista, y se ejecuta el bloque de código dentro del bucle.
En este caso, se imprime cada fruta en una línea separada.
"""
 
# While

"""
Se utiliza para repetir un bloque de código mientras una condición sea verdadera.
"""

"""
La sintaxis básica es la siguiente:

while condicion:

    # Bloque de código a repetir
    instrucciones
"""

contador = 0

while contador < 5:

    print(contador)
    contador += 1


"""
En este ejemplo, el bucle while se ejecuta mientras la variable contador sea menor que 5.
En cada iteración, se imprime el valor de contador y luego se incrementa en 1 mediante la instrucción contador += 1.
El bucle se detendrá cuando contador alcance el valor de 5.


***Es importante tener cuidado al usar el bucle while, ya que, si la condición nunca se vuelve falsa,
***el bucle se ejecutará indefinidamente, lo que se conoce como un bucle infinito.

"""

