def RevNo(No):
    rev = "" 
    for ch in No:
        rev = ch + rev
    return rev

def main():
    Val = input("Enter a No : ")
    Ret = RevNo(Val)

    print("Rev is : ",Ret)

if __name__ == "__main__":
    main()