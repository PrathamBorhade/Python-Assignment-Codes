Max = lambda No1,No2 : No1 > No2 

def main():
    No1 = int(input("Enter First No : "))
    No2 = int(input("Enter Second No : "))

    Ret = Max(No1,No2)

    if(Ret == True):
        print("Maximum is :",No1)
    else:
        print("Maximum is :",No2)

if __name__ == "__main__":
    main()