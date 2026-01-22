def Perfect(No):
    sum = 0
    for i in range(1,No):
        if(No % i==0):
            sum += i
    return sum

def main():
    No = int(input("Enter a No : "))
    Ret = Perfect(No)

    if(No == Ret):
        print("Perfect No")
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()