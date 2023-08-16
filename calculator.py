# addition
def add(x, y):
    return x + y

# substract
def substract(x, y):
    return x - y

# Multiply
def multiply(x ,y):
    return x * y

# divide
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by ZERO!")

# select menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice : ")

# number input
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Secound Numberc : "))

if choice == "1":
    print("Result : ", add(num1, num2))
elif choice == "2":
    print("Result : ", substract(num1, num2))
elif choice == "3":
    print("Result : ", multiply(num1, num2))
elif choice == "4":
    print("Result : ", divide(num1, num2))
else:
    print("Invalid choice!")