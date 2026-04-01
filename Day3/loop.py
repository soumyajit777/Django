# sum of first ten natural numbers
n = int(input("Enter a natural number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i

print("The sum is ", sum)