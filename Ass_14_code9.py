Mult = lambda No1,No2 : No1 * No2 

def main():
    No1 = int(input("Enter First No : "))
    No2 = int(input("Enter Second No : "))
    
    Ret = Mult(No1,No2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()