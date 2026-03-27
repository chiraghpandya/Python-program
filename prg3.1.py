# wap to create simple class with 2 method and execute both method
class MyClass:
    def method1(self): #self refers to current object
        print("Hi,i am method1")
    def method2(self): #seld refers to current object
        print("Hello,i am method2")


obj=MyClass()
obj.method1()
obj.method2()
