#student grade

name=input("Enter Your Name:")
per=int(input("Enter Percentage:"))
print(f"Name Of Student Is {name}")

if per>=90:
    print("grade Of Student is O:")

elif per>=70 and per<90:
    print("grade  Of Student is A+:")

elif per>=50 and per<70:
    print("grade Of Student is A:")

elif per>=40 and per<50:
    print("grade Of Student is B:")

else :
    print("Fail:")
