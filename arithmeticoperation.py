#arithmetic operation

n1=float(input("enter first number:")) #enter 1 number
n2=float(input("enter second number:")) #enter 2 number
ch=input("enter your choice:+,-,*,/") #user choice

#match case 
match(ch):
    case '+':
        add=n1+n2
        print("addition is:",add)

    case '-':
        sub=n1-n2
        print("subtraction is:",sub)

    case '*':
        mul=n1*n2
        print("multipliocation is:",mul)

    case '/':
        div=n1/n2
        print("dividion is:",div)

    case _:
        print("invalid choice:")
