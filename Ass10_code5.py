def Odd(No):
    data = []
    for i in range(1,No+1,2):
        data.append(i)
    return data

def main():
    Num = int(input("Enter a number : "))

    Ret = Odd(Num)
    print("Odd numbers :",Ret)

if __name__ =="__main__":
    main()