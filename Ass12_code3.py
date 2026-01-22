def Add(No1,No2):
    Add = 0
    Add = No1 + No2
    return Add

def Sub(No1,No2):
    Sub = 0
    Sub = No1 - No2
    return Sub

def Div(No1,No2):
    Div = 0
    Div = No1 / No2
    return Div

def Mult(No1,No2):
    Mult = 0
    Mult = No1 * No2
    return Mult

def main():
    No1 = int(input("Enter first No : "))
    No2 = int(input("Enter second No : "))
    
    print("Addition is ",Add(No1,No2))
    print("Substraction is ",Sub(No1,No2))
    print("Division is ",Div(No1,No2))
    print("Multiplication is ",Mult(No1,No2))

if __name__ == "__main__":
    main()