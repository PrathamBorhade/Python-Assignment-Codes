def Sum(No):
    Sum = 0
    for i in range(No+1):
        Sum = Sum + i

    return Sum 

def main():
    Num = int(input("Enter a number : "))

    Ret = Sum(Num)
    print("Sum of first",Num,"nos is : ",Ret)

if __name__ =="__main__":
    main()