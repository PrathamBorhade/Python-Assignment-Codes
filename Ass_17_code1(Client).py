import Ass_17_code1_Module

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Res = Ass_17_code1_Module.Add(No1,No2)
    print("Addition is : ",Res)

    Res = Ass_17_code1_Module.Sub(No1,No2)
    print("Substraction is :",Res)

    Res = Ass_17_code1_Module.Div(No1,No2)
    print("Division is :",Res)

    Res = Ass_17_code1_Module.Mult(No1,No2)
    print("Multiplication is :",Res)

if __name__ == "__main__":
    main()