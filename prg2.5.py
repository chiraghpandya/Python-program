'''5. Write a function inside another function.'''

def calculate(a,b):
    def add():
        return a + b

    def multiply():
        return a * b

    print("Addition:",add())
    print("Multiplication :",multiply())

calculate(5, 3)
