class circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of circle : "))

    def CalculateArea(self):
        self.Area = 0
        self.Area = self.PI*(self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 0
        self.Circumference = 2*self.PI*self.Radius

    def Display(self):
        print("Radius of circle is : ",self.Radius)        
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)

obj1 = circle()
obj2 = circle()

obj1.Accept()
obj2.Accept()

obj1.CalculateArea()
obj2.CalculateArea()

obj1.CalculateCircumference()
obj2.CalculateCircumference()

obj1.Display()
obj2.Display()