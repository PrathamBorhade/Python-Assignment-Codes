def ChkDiv(Value):
    if(Value!=3 and Value!=5):
        return True
    else:
        return False

def main():
    print("Enter No : ")
    No = int(input())
    Result = ChkDiv(No)
    if(Result==True):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")


if __name__ == "__main__":
    main()