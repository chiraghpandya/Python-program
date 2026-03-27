#wap to make use of class method and instance method

class Student:
    def __init__(self,Rollno,Name,age,gender):
        self.Rollno= Rollno
        self.Name= Name
        self.age= age
        self.gender= gender

    def Displaystudent(self):
        print("\n----Student Detail----")
        print("Rollno:",self.Rollno)
        print("Name:",self.Name)
        print("age:",self.age)
        print("gender:",self.gender)

s1=Student(7,"Chirag",21,"Male")
s1.Displaystudent()
