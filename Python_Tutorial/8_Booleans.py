# Booleanos de Python
"""
Valores booleanos
En programación, a menudo necesitas saber si una expresión es Trueo False.

Puede evaluar cualquier expresión en Python y obtener una de dos respuestas, Trueo False.

Cuando compara dos valores, la expresión se evalúa y Python devuelve la respuesta booleana:
"""
# Ejemplo
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


# Cuando ejecuta una condición en una declaración if, Python devuelve Trueo False:

# Ejemplo

# Imprime un mensaje basado en si la condición es Trueo False:
# a = 200
# b = 33
# if b > a:
#     # print("b is greater than a")
# else:
#     # print("b is not greater than a")


# Evaluar valores y variables
# La bool()función te permite evaluar cualquier valor, y darte Trueo False a cambio,

# Ejemplo
# Evaluar una cadena y un número:
# print(bool("Hello"))
# print(bool(15))


# Ejemplo
# Evalúa dos variables:

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

"""
La mayoría de los valores son verdaderos
Casi cualquier valor se evalúa Truesi tiene algún tipo de contenido.

Cualquier cadena es True, excepto las cadenas vacías.

Cualquier número es True, excepto 0.

Cualquier lista, tupla, conjunto y diccionario son True, excepto los vacíos.
"""

# Ejemplo
# Lo siguiente devolverá True:
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))


"""
Algunos valores son falsos
De hecho, no hay muchos valores que se evalúen como False, excepto valores vacíos, como (), [], {}, "", el número 0y el valor None. Y, por supuesto, el valor Falsese evalúa como False.
"""

# Ejemplo
# Lo siguiente devolverá Falso:
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# Un valor más, u objeto en este caso, se evalúa como False, y eso es si tiene un objeto que se crea a partir de una clase con una __len__función que devuelve 0o False:

# class myclass():
#     def __len__(self):
#         return 0

# myobj = myclass()
# print(bool(myobj))




# Las funciones pueden devolver un valor booleano
# Puede crear funciones que devuelvan un valor booleano:

# Ejemplo
# Imprime la respuesta de una función:

# def myFunction():
#     return True

# print(myFunction())





# Puede ejecutar código basado en la respuesta booleana de una función:

# Ejemplo
# Imprimir "¡SÍ!" si la función devuelve True, de lo contrario imprime "¡NO!":

# def myFunction():
#     return True

# if myFunction():
#     print("YES")
# else:
#     print("No!")


# Python también tiene muchas funciones integradas que devuelven un valor booleano, como la isinstance() función, que se puede usar para determinar si un objeto es de cierto tipo de datos:


# Ejemplo
# Compruebe si un objeto es un número entero o no:

# x = 200
# print(isinstance(x, int))