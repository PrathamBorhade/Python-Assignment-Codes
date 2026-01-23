Max = lambda No1,No2,No3 : No1 > No2 and No1 > No3

def main():
    No1 = int(input("Enter First No : "))
    No2 = int(input("Enter Second No : "))
    No3 = int(input("Enter Third No : "))

    Ret = Max(No1,No2,No3)
    Res = Max(No2,No3,No1)

    if(Ret == True):
        print("Largest is :",No1)
    elif(Res == True):
        print("Largest is :",No2)
    else:
        print("Largest is :",No3)
        
if __name__ == "__main__":
    main()