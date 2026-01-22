def SumNo(No):
    sum = 0
    for dig in No:
        sum = sum + int(dig)
    return sum

def main():
    Val = input("Enter a No : ")
    Ret = SumNo(Val)

    print("Sum is : ",Ret)

if __name__ == "__main__":
    main()

