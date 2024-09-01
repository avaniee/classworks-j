def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiplty(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Please select your operation method:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please enter your choice (1/2/3/4): ")

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("You have an invalid input!")

