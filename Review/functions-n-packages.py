def greet(name, age):
    print(f"Hello {name}, I am {age} years old!")

greet("Cincin", 21)  

#lowercase & uppercase
msg = "wah haffen vella"
print(msg.upper())

#replaces the word
print(msg.replace("vella", "diwata"))

#sorts and reverses integers
numeros = [3,4,9,5]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

#------------PACKAGES--------------
import math
print("Square root of 16: ")
print (math.sqrt(16))

# from math import pi
# print(pi)             #selective import

# import math as m
# print(m.sqrt(25))      

# from math import sqrt as s
# print(s(49))           

