def ChkPrime(No):
    for i in range(2,No):
        if(No%i == 0):
            return False
        else:
            return True

def main():
    Val = int(input("Enter a No : "))
    Ret = ChkPrime(Val)

    if(Ret == True):
        print("Prime number")
    else:
        print("Not a Prime number")

if __name__ == "__main__":
    main()