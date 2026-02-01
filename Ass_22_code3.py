class Demo:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value : "))
        self.Value2 = int(input("Enter Second value : "))

    def Addition(self):
        self.Sum = 0
        self.Sum = self.Value1 + self.Value2
        print("Addition is : ",self.Sum)

    def Substraction(self):
        self.Sub = 0
        self.Sub = self.Value1 - self.Value2
        print("Substraction is : ",self.Sub)

    def Multiplication(self):
        self.Mul = 0
        self.Mul = self.Value1 * self.Value2
        print("Multiplication is : ",self.Mul)

    def Division(self):
        self.Div = 0
        if(self.Value2 == 0):
            print("Error : Division by zero ")
        else:
            self.Div == self.Value1/self.Value2
            print("Division is : ",self.Div)

obj1 = Demo()
obj2 = Demo()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()

print("~"*60)

obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()