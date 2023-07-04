# Python Operators

"""Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:"""

# print(10 + 5)

"""
Python divide a los operadores en los siguientes grupos:

Operadores aritméticos
Operadores de Asignación
Operadores de comparación
Operadores logicos
Operadores de identidad
Operadores de membresía
Operadores bit a bit
"""


"""
Operadores aritméticos de Python
Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones matemáticas comunes:"""

"""
+	Addition	    x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""


"""Operadores de asignación de Python

Los operadores de asignación se utilizan para asignar valores a las variables:"""

"""
=	    x = 5	    x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3 	x = x // 3	
**=	    x **= 3 	x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=    	x >>= 3 	x = x >> 3	
<<=	    x <<= 3 	x = x << 3
"""



"""
Operadores de comparación de Python
Los operadores de comparación se utilizan para comparar dos valores:
"""
"""
==	    Equal	                    x == y	
!=	    Not equal	                x != y	
>	    Greater than	            x > y	
<	    Less than	                x < y	
>=	    Greater than or equal to	x >= y	
<=	    Less than or equal to	    x <= y
"""




"""
Operadores lógicos de Python
Los operadores lógicos se utilizan para combinar sentencias condicionales:
"""
"""
and 	Returns True if both
         statements are true	        x < 5 and  x < 10

or	    Returns True if one of the 
        statements is true	            x < 5 or x < 4	

not 	Reverse the result, returns 
        False if the result is true 	not(x < 5 and x < 10)
"""


"""
Operadores de identidad de Python
Los operadores de identidad se utilizan para comparar los objetos, no si son iguales, sino si en realidad son el mismo objeto, con la misma ubicación de memoria:
"""
"""
is 	    Returns True if both variables
        are the same object	                x is y	

is not	Returns True if both variables 
        are not the same object         	x is not y
"""


"""
Operadores de membresía de Python
Los operadores de membresía se utilizan para probar si una secuencia se presenta en un objeto:
"""

"""
in 	        Returns True if a sequence
            with the specified value is 
            present in the object	            x in y	

not in	    Returns True if a sequence 
            with the specified value is
            not present in the object	        x not in y
"""


"""
Operadores bit a bit de Python
Los operadores bit a bit se utilizan para comparar números (binarios):
"""

"""
& 	    AND	    Sets each bit to 1
                if both bits are 1	        x & y	

|	    OR	    Sets each bit to 1 
                if one of two bits is 1     x | y

^	    XOR	    Sets each bit to 1 if
                only one of two bits is 1	x ^ y	

~	    NOT	    Inverts all the bits	    ~x	

<<	    Zero fill   Shift left by pushing    x << 2
        left shift	zeros in from the right 
                    and let the leftmost bits 
                    fall off 
          	                    


>>	    Signed      Shift right by pushing copies of the                 leftmost bit in from the left, and let the 
                        rightmost bits fall off	x >> 2
        right shift
            	
"""