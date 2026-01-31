class Demo:
    Value = 0

    def __init__(self,No1,No2):
        self.value1 = No1
        self.value2 = No2

    def Fun(self):
        print("Values of Instance variables from Fun are : ",self.value1,self.value2)

    def Gun(self):
        print("Values of Instance variables from Gun are : ",self.value1,self.value2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()

obj2.Fun()
obj1.Gun()
obj2.Gun()