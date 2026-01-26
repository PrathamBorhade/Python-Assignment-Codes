def ChkNum(No):
    if(No%2==0):
        return True
    else:
        return False

def main():
    No = int(input("Enter a No : "))

    Res = ChkNum(No)
    if(Res==True):
        print("Even Number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()