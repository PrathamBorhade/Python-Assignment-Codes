def MultTable(No):
    for i in range(1,11):
        Ans = No * i

    return Ans

def main():
    print("Enter the number : ")
    val = int(input())

    Ret = MultTable(val)
    for i in range(1,11):
        print(val,"*",i,"=",Ret)

if __name__ == "__main__":
    main()