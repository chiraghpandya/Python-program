# write a program to find positive and negavtive value

a=int(input("Enter Number To Check Positive Or Negative:"))

if a%2>0:
    print("Number is Positive:",a)

elif a%2<0:
    print("Number is Negative:",a)

else:
    print("Number is Equal to Zero:",a)
