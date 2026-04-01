# Program of swapping two numbers without using any third variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swapping a = {} and b = {}".format(a, b))

a = a + b
b = a - b
a = a - b

print("After swapping a = {} and b = {}".format(a, b))