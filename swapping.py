# swapping values

a=int(input("Enter value of first number: "))
b=int(input("Enter value of second number:"))
print(f"before swapping :\n value 1 is:{a} \n value 2 is:{b}")

a=a+b
b=a-b
a=a-b
print(f"after swapping :\n value 1 is:{a} \n value 2 is:{b}")
