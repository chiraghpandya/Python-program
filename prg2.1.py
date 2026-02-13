'''1. Write a Function to Perform Arithmetic Operations
 Create separate functions for addition,
subtraction, multiplication, and division.
 Call them based on user input.'''

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("arithmetic operation:")
print("1. Addition:")
print("2. Subtraction:")
print("3. Multiplication:")
print("4. Division:")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

ch = int(input("Enter your choice (1-4):"))

if ch == 1:
    result = add(num1,num2)
elif ch == 2:
    result = sub(num1,num2)
elif ch == 3:
    result = mul(num1,num2)
elif ch == 4:
    result = div(num1,num2)
else:
    result = "Invalid choice:"

print("Result:",result)




