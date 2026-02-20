#a=7
#b=7
#c=a+b
#print(c)

a=int(input("enter first number:"))
b=int(input("enter second number:"))

ch=input("enter your choice + - * /:")

ans=0
if ch=='+':
    ans=a+b
elif ch=='-':
    ans=a-b
elif ch=='*':
    ans=a*b
elif ch=='/':
    ans=a/b
else:
    print("input is wrong")

print("ans is:",ans)
