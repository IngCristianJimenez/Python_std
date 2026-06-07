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

"""Ejemplo:

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

"""