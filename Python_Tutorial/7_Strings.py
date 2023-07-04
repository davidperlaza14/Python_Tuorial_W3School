# Python Strings
"""
Las cadenas en python están entre comillas simples o comillas dobles.

'hola' es lo mismo que 'hola' .

Puede mostrar un literal de cadena con la print()función:
"""

# Ejemplo
# print("Hello")
# print('Hello')

"""
La asignación de una cadena a una variable se realiza con el nombre de la variable seguido de un signo igual y la cadena:"""
# Ejemplo
# a = "Hello"
# print(a)


# Multiline Strings

# Puede asignar una cadena de varias líneas a una variable usando tres comillas:

# Ejemplo
# Puede utilizar tres comillas dobles:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)


# Strings are Arrays

"""Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres Unicode.

Sin embargo, Python no tiene un tipo de datos de caracteres, un solo carácter es simplemente una cadena con una longitud de 1.

Se pueden usar corchetes para acceder a elementos de la cadena."""

# Ejemplo
# Obtenga el carácter en la posición 1 (recuerde que el primer carácter tiene la posición 0):

a = "Hello, World!"
# print(a[1])


"""Bucle a través de una cadena
Dado que las cadenas son matrices, podemos recorrer los caracteres de una cadena, con un forbucle."""

# Ejemplo
# Repasa las letras de la palabra "banana":

# for x in "Banana":
#     print(x)


# String Length

"""Para obtener la longitud de una cadena, use la len()función."""

# Ejemplo
# La len()función devuelve la longitud de una caden

a = "Hello, World!"
# print(len(a))


# Check String

"""Para verificar si una determinada frase o carácter está presente en una cadena, podemos usar la palabra clave in."""

# Ejemplo
# Compruebe si "gratis" está presente en el siguiente texto:

# txt = "The best things in life are free!"
# print("free" in txt)


# Úselo en una ifdeclaración:

# Ejemplo
# Imprima solo si "gratis" está presente:
# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")


# Check if NOT

# Para verificar si una determinada frase o carácter NO está presente en una cadena, podemos usar la palabra clave not in.

# Ejemplo
# Compruebe si "caro" NO está presente en el siguiente texto:
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# Úselo en una ifdeclaración
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#     print("No, 'expensive' is NOT present")


# ===========================================
# Python - Slicing Strings

# rebanar
# Puede devolver un rango de caracteres utilizando la sintaxis de división.

# Especifique el índice inicial y el índice final, separados por dos puntos, para devolver una parte de la cadena.

# Ejemplo
# Obtenga los caracteres de la posición 2 a la posición 5 (no incluidos):
 
# b = "Hello, World"
# print(b[2:5])

# Cortar desde el principio
# Al omitir el índice de inicio, el rango comenzará en el primer carácter:

# b = "Hello, World!"
# print(b[:5])


# Cortar hasta el final
# Al omitir el índice final , el rango irá hasta el final:

# Ejemplo
# Consigue los personajes desde la posición 2 y hasta el final:


# b = "Hello, World!"
# print(b[2:])

# Indexación negativa
# Utilice índices negativos para iniciar el segmento desde el final de la cadena:



# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
# b = "Hello, World!"
# print(b[-5:-2])

# ==============================================
# Python - Modify Strings

# Upper
# Ejemplo
# El upper()método devuelve la cadena en mayúsculas:

a = "Hello, world!"
# print(a.upper())


# Lower
# Ejemplo
# El lower()método devuelve la cadena en minúsculas:
b = "Hello, world1"
# print(b.lower())



# Eliminar espacios en blanco
# El espacio en blanco es el espacio antes y/o después del texto real, y muy a menudo desea eliminar este espacio.

# Ejemplo
# El strip()método elimina cualquier espacio en blanco desde el principio o el final:

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"



# Reemplazar cadena
# Ejemplo
# El replace()método reemplaza una cadena con otra cadena:

# a = "Hello, World!"
# print(a.replace("H", "D"))

# Cadena dividida
# El split()método devuelve una lista donde el texto entre el separador especificado se convierte en los elementos de la lista.

# Ejemplo
# El split()método divide la cadena en subcadenas si encuentra instancias del separador:

# a = "Hello, World!"
# print(a.split(","))# returns ['Hello', ' World!']


# ======================================
# Python - String Concatenation
# Concatenación de cadenas
# Para concatenar o combinar dos cadenas, puede usar el operador +.

# Ejemplo 
# Combinar variable acon variable ben variable c:
a = "Hello"
b = "World"
c = a + b
# print(c)


# Ejemplo
# Para agregar un espacio entre ellos, agregue un " ":

a = "Hello"
b = "World"
c = a + " " + b
# print(c)




# ===================================
# Python - Format - Strings

# Formato de cadena
# Como aprendimos en el capítulo Variables de Python, no podemos combinar cadenas y números como este:

# Ejemplo
age = 36
# txt = "My name is John, I am " + age
# print(txt)


# ¡Pero podemos combinar cadenas y números usando el format()método!

# El format()método toma los argumentos pasados, les da formato y los coloca en la cadena donde {}están los marcadores de posición:

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# El método format() toma un número ilimitado de argumentos y se colocan en los marcadores de posición respectivos:


# Ejemplo
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# Puede usar números de índice {0}para asegurarse de que los argumentos se colocan en los marcadores de posición correctos:


# Ejemplo
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))



# =============================================
# Python - Escape Characters

# Para insertar caracteres que no son válidos en una cadena, utilice un carácter de escape.

# Un carácter de escape es una barra invertida \seguida del carácter que desea insertar.

# Un ejemplo de un carácter ilegal es una comilla doble dentro de una cadena que está entre comillas dobles:


# Ejemplo
# Obtendrá un error si usa comillas dobles dentro de una cadena que está entre comillas dobles:

# txt = "We are the so-called "Vikings" from the north."


# Para solucionar este problema, utilice el carácter de escape \":

# Ejemplo
# El carácter de escape le permite usar comillas dobles cuando normalmente no se le permitiría:

txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



