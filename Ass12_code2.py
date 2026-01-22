def Factors(No):
    Fact = []
    for i in range(1,No+1):
        if(No%i==0):
            Fact.append(i)
    return Fact

def main():
    No = int(input("Enter a No : "))
    Ret = Factors(No)

    print("Factors are : ",Ret)

if __name__ == "__main__":
    main()