'''3. Function to Calculate Factorial (Using Recursion)
 Implement factorial using:
o Normal function
o Recursive function'''

def factorial(n):
    if n < 0:
        return "Factorial does not exists for negative number:"

    fact = 1
    for i in range (1, n + 1):
        fact = fact * 1

        return fact

#main program
num1 = int(input("Enter Number:"))
result = factorial(num)

print("Factorial is :",result)
