from functools import reduce

def main():
    lst = []
    No = int(input("Enter No of elements : "))

    print("Enter the numbers : ")

    for i in range(No):
        Val = int(input())
        lst.append(Val)

    print("List is : ",lst)

    flst = list(filter(lambda No : No%2==0,lst))
    print("Data after filter : ",flst)

    mlst = list(map(lambda No : No**2,flst))
    print("Data after Map : ",mlst)

    rlst = reduce(lambda No1, No2 : No1 + No2,mlst)
    print("Addition of all elements : ",rlst)

if __name__ == "__main__":
    main()        