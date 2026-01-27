import MarvellousNum

def ListPrime(lst):
    chk = []
    sum = 0
    for No in lst:
        if(MarvellousNum.ChkPrime(No)):
            chk.append(No)
            sum += No
    return chk,sum

def main():
    No = int(input("Enter No of elements : "))
    print("Enter the numbers : ")
    
    lst = []
    
    for i in range(No):
        Val = int(input())
        lst.append(Val)


    print("List is ",lst)

    prime, sum = ListPrime(lst)
    print("Prime numbers are : ",prime)
    print("Sum is : ",sum)    
    
if __name__ == "__main__":
    main()        