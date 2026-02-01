class Numbers:
    
    def __init__(self):
        self.Value = int(input("Enter the Number : "))



    def ChkPrime(self):
        for i in range(2,self.Value):
            if(self.Value%i==0):
                print(f"{self.Value} is not a Prime Number")
                break
            else:
                print(f"{self.Value} is a Prime Number")
                break
    
    def Factors(self):
        self.Fact = []
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                self.Fact.append(i)
        print(f"Factors of {self.Value} are : ",self.Fact)

    def SumFactors(self):
        self.sum = 0
        for i in range(1,self.Value):
            if(self.Value%i==0):
                self.sum += i
        print("Sum is : ",self.sum)

    def ChkPerfect(self):
        if(self.sum == self.Value):
            print(f"{self.Value} is a perfect no")
        else:
            print(f"{self.Value} is not a Perfect no")


obj1 = Numbers()

obj1.ChkPrime()
obj1.Factors()
obj1.SumFactors()
obj1.ChkPerfect()

print("-"*50)

obj2 = Numbers()

obj2.ChkPrime()
obj2.Factors()
obj2.SumFactors()
obj2.ChkPerfect()