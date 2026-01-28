from functools import reduce

def ChkPrime(No):
    for i in range(2,No):
        if(No%i==0):
            return False
    return True

def Maximum(No1,No2):
    if (No1 > No2):
        return No1
    else:
        return No2    

def main():
    lst = []
    No = int(input("Enter No of elements : "))

    print("Enter the numbers : ")

    for i in range(No):
        Val = int(input())
        lst.append(Val)

    print("List is : ",lst)

    flst = list(filter(ChkPrime,lst))
    print("Data after filter : ",flst)

    mlst = list(map(lambda No : No*2,flst))
    print("Data after Map : ",mlst)

    rlst = reduce(Maximum,mlst)
    print("Maximum is : ",rlst)

if __name__ == "__main__":
    main()        