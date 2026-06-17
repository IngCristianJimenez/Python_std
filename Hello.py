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

print ("Números del 1 al 5 multiplicados por 2 con bucle FOR:")
for numero in range(1,6):
    print (numero * 2)

print ("\n Números del 1 al 5 multiplicados por 2 con el bucle WHILE:")
contador = 1
while contador <=5:
    print (contador * 2)
    contador += 1


# ***Control de bucles***

# Python proporciona algunas instrucciones especiales para controlar el flujo de ejecución dentro de los bucles: 

"""
Break

La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición.
Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.


"""

print("\n Contador con \"BREAK\": ")
contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
    

"""
   *** Continue ***
   
La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.
"""

# Ejemplo:

print ("\n Contador con \"CONTINUE\": ")
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

    
"""
En este ejemplo, el bucle for itera sobre los números del 0 al 9 utilizando la función range().
Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %.
Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción continue,
lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle.
Como resultado, solo se imprimirán los números impares.
"""


"""
   *** Pass ***

La instrucción pass es una operación nula que no hace nada.
Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción.
"""
print ("\n Contador con instrucción \"PASS\": ")

# Ejemplo:

for i in range(5):
    pass

"""
En este ejemplo, el bucle for itera sobre los números del 0 al 4,
pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass.
Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.
"""


print ("\n 4.- Estructuras de Datos")

"""
Las estructuras de datos nos permiten organizar y almacenar datos de manera eficiente en nuestros programas.
Python proporciona varias estructuras de datos integradas, como listas, tuplas, diccionarios y conjuntos,
cada una con sus propias características y usos.
"""


print("\n Listas: ")

"""
Una lista es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos.
Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes [], separados por comas.
"""

# Creación y acceso

# Para crear una lista, simplemente encierra los elementos entre corchetes:

frutas = ["manzana", "banana", "naranja"]

print ("\n Lista 0,1,2\n")
print (frutas[0]) # Imprime manzana
print (frutas[1]) # Imprime banana
print (frutas[2]) # Imprime naranja


"""
También puedes acceder a los elementos desde el final de la lista utilizando índices negativos.
El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.
"""
print ("\n Lista -1,-2 y -3\n")
print (frutas[-1]) # Imprime naranja
print (frutas[-2]) # Imprime banana
print (frutas[-3]) # Imprime manzana

print("\n Métodos de listas")

# Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista.

# Algunos métodos comunes son:

"""
append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista.
"""

frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]


# ***Listas de comprensión***
print("\n Listas de Comprensión: \n")
# Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente.
# Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

# nueva_lista = [expresion for elemento in secuencia if condicion]


# Ejemplo:

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# En este ejemplo, se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista numeros.
# La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.




# *** Tuplas ***
print("\n Tuplas: ")

"""
Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos.
Los elementos de una tupla se encierran entre paréntesis (), separados por comas.
"""

# Creación y acceso


# Para crear una tupla, encierra los elementos entre paréntesis:

punto = (3, 4)

#Para acceder a los elementos de una tupla, utiliza el índice del elemento entre corchetes, similar a las listas:

print(punto[0])  # Imprime 3

print(punto[1])  # Imprime 4

"""
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.
No se pueden agregar, eliminar o cambiar elementos en una tupla existente.

Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse,
como coordenadas o datos de configuración.
"""



# *** Métodos de tuplas ***
print("\n Métodos de Tuplas: \n")

"""
Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

- count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 

- index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente,
se puede especificar el inicio y fin de la búsqueda. 

- len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.

"""

mi_tupla = (1, 2, 3, 2, 4, 2)


print (mi_tupla.index(2))   # Salida: 1

print (mi_tupla.index(2, 2))   #Salida: 3

print (mi_tupla.index(2, 2, 4))   #Salida: 3



print("\n Diccionarios: \n")

"""
Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor.
Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves {},
y los pares clave-valor se separan por comas.
"""
 

# Creación y acceso

# Para crear un diccionario, utiliza llaves y separa las claves y valores con dos puntos.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

# También puedes utilizar el método get() para obtener el valor de una clave.
# Si la clave no existe, devuelve un valor predeterminado (por defecto, None).


print("\n Métodos de diccionarios: \n")

"""
Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:
"""

# - keys(): devuelve una vista de todas las claves del diccionario.
# - values(): devuelve una vista de todos los valores del diccionario.
# - items(): devuelve una vista de todos los pares clave-valor del diccionario.
# - update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.


# Ejemplo:

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

