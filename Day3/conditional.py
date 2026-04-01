age = int(input("Enter age: "))

# Program to check eligibility for vote
if (age >= 18):
    print("You're eligible for vote")
else:
    print("You're not eligible for vote")


# Program to check whether the person is kid, child, teen or adult
if (age > 0 and age <= 5):
    print("You are a kid")
elif (age <= 11):
    print("You are a child")
elif (age <= 19):
    print("You are a teen")
else:
    print("You are an adult")