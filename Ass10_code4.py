def Even(No):
    data = []
    for i in range(2,No+1,2):
        data.append(i)
    return data

def main():
    Num = int(input("Enter a number : "))

    Ret = Even(Num)
    print("Even numbers :",Ret)

if __name__ =="__main__":
    main()