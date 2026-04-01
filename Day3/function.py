# Function declaration
def add():
    a = 10
    b = 20
    c = a + b
    print("Addition:", c)

add() #Function call

def add(a, b):
    a = a + b 
    return a

res = add(30, 20)
print("Addition:", res)