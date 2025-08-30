#What are Operators?
#Operators are special symbols used to perform operations on variables and values.

#1. Arithmetic Operators
#Used for mathematical operations.
#+ (Addition)
#- (Subtraction)
#* (Multiplication)
#/ (Division - float result)
# (Floor Division - integer result)
#% (Modulus - remainder)
#** (Exponent - power)

# Example:
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

#2. Comparison (Relational) Operators
#Used to compare values (returns True or False).
#== (Equal to)
#!= (Not equal to)
#> (Greater than)
#< (Less than)
#>= (Greater than or equal to)
#<= (Less than or equal to)

#✅ Example:
a, b = 5, 10
print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 5)   # True
print(b <= 5)   # False

#3. Logical Operators
#Used to combine conditions.
#and (True if both are true)
#or  (True if at least one is true)
#not (Negates the result)

#✅ Example:
x = True
y = False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False

#4. Assignment Operators
#Used to assign values to variables.
#= (Simple assign)
#+= (Add and assign)
#-= (Subtract and assign)
#*= (Multiply and assign)
#/= (Divide and assign)
#%= (Modulus and assign)
#**= (Power and assign)
#//= (Floor divide and assign)

#✅ Example:
a = 10
a += 5   # a = a + 5
print(a) # 15

#5. Bitwise Operators (works on binary numbers)
#& (AND)
#| (OR)
#^ (XOR)
#~ (NOT)
#<< (Left shift)
#>> (Right shift)

#✅ Example:
a, b = 6, 3  # binary: 6 = 110, 3 = 011
print(a & b)   # 2 (010)
print(a | b)   # 7 (111)
print(a ^ b)   # 5 (101)
print(~a)      # -7
print(a << 1)  # 12
print(a >> 1)  # 3

#6. Identity Operators
#is → True if two objects are same.
#is not → True if not same.

#✅ Example:
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)      # True (same object in memory)
print(x is z)      # False (different objects)
print(x is not z)  # True

#7. Membership Operators
#in → True if value exists.
#not in → True if value does not exist.
#✅ Example:

list1 = [1,2,3,4]
print(2 in list1)       # True
print(10 not in list1)  # True

