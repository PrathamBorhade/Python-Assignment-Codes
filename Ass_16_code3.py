def Add(No1,No2):
    add = 0
    add = No1 + No2
    return add

def main():
    No1 = int(input("Enter First No : "))
    No2 = int(input("Enter Second No : "))
    Res = Add(No1,No2)

    print("Addition is :",Res)
    
if __name__ == "__main__":
    main()