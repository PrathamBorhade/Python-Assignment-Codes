def RevNo(No):
    rev = "" 
    for ch in No:
        rev = ch + rev
    return rev

def main():
    Val = input("Enter a No : ")
    Ret = RevNo(Val)

    if(Val == Ret):
        print("It is a palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    main()