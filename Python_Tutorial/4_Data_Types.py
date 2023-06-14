"""Python Data Types"""

# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

"""
Text Type:	            str
Numeric Types:	        int, float, complex
Sequence Types:     	list, tuple, range
Mapping Type:	        dict
Set Types:	            set, frozenset
Boolean Type:	        bool
Binary Types:	        bytes, bytearray, memoryview
None Type:	            NoneType
"""

# Getting the Data Type
# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

a = "Hello World"
print(a)
print(type(a))

b = 20
print(b)
print(type(b))

c = 20.5
print(c)
print(type(c))

d = 1j
print(d)
print(type(d))

e = ["Apple", "Banana", "cherry"]
print(e)
print(type(e))

f = ("Apple", "Banana", "cherry")
print(f)
print(type(f))

g = frozenset({"Apple", "Banana",
                "cherry"})
print(g)
print(type(g))

h = True
print(h)
print(type(h))

i = b"Hello"
print(i)
print(type(i))

j =  bytearray(5)
print(j)
print(type(j))

k = memoryview(bytes(5))
print(k)
print(type(k))

l = None
print(l)
print(type(l))

m = range(6)
print(m)
print(type(m))

n = {"name": "David", "ege": 23}
print(n)
print(type(n))

o = {"Apple", "Banana", "cherry"}
print(o)
print(type(o))



