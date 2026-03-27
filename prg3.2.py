#wap to display student detail with 2 method
class Student:
    def Addstudent(self):
        self.Rollno=int(input("Enter your rollno:"))
        self.Name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.gender=input("Enter your gender:")

    def Displaystudent(self):
        print("\n----Student Detail----")
        print("Rollno:",self.Rollno)
        print("Name:",self.Name)
        print("age:",self.age)
        print("gender:",self.gender)

s1=Student()
s1.Addstudent()
s1.Displaystudent()
