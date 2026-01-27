def List(No):
    lst = []
    
    for i in range(No):
        Val = int(input())
        lst.append(Val)
    return lst

def Minimum(lst):
    Min = lst[0]
    for Val in lst:
        if(Min > Val):
            Min = Val
    return Min

def main():
    
    No = int(input("Enter No of elements : "))

    print("Enter the numbers : ")
    
    Res = List(No)
    print("List is ",Res)
    print("Minimum is : ",Minimum(Res))
    
    
if __name__ == "__main__":
    main()