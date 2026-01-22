def PrintNo(No):
    Fact = []
    for i in range(1,No+1):
        Fact.append(i)
    return Fact

def main():
    No = int(input("Enter a No : "))
    Ret = PrintNo(No)

    print("Numbers are : ",Ret)

if __name__ == "__main__":
    main()