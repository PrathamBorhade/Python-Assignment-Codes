def ChkPrime(No):
    for i in range(2,No):
        if(No%i==0):
            return True
        else:
            return False

def main():
    No = int(input("Enter a number : "))
    Res = ChkPrime(No)

    if(Res==True):
        print("Not a prime number ")
    else:
        print("Prime number")

if __name__ == "__main__":
    main()