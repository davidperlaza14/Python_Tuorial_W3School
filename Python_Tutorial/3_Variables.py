

"""
Creación de variables
Python no tiene ningún comando para declarar una variable.

Una variable se crea en el momento en que le asigna un valor por primera vez."""

x = 5
y = "John"


# Variable Names
#  Example

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Example
# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"



# Multi Words Variable Names

# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"



# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "David"


# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "Stiven"



# Python Variables - Assign Multiple Values

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

# Example

x, y, z = "Orange", "Banana", "Cherry"
# print(x, z, y)



# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print()


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# Python - Output Variables
# The Python print() function is often used to output variables.

# In the print() function, you output multiple variables, separated by a comma:

# Example

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:

# Example
x = 5
y = 10
print(x + y)



# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# Example
x = 5
y = "John"
# print(x + y)


# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

# Example
x = 5
y = "John"
print(x, y)


# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

# Example
# Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
    print("Python is " + x)

# myfunc()


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# Example
# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

# myfunc()

# print("Python is " + x)



# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Example
# If you use the global keyword, the variable belongs to the global scope:


def myfunc():
    global x
    x = "fantastic"

myfunc()

# print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





