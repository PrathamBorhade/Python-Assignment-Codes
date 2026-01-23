Min = lambda No1,No2 : No1 > No2 

def main():
    No1 = int(input("Enter First No : "))
    No2 = int(input("Enter Second No : "))

    Ret = Min(No1,No2)

    if(Ret == True):
        print("Minimum is :",No2)
    else:
        print("Minimum is :",No1)

if __name__ == "__main__":
    main()