def List(No):
    lst = []
    
    for i in range(No):
        Val = int(input())
        lst.append(Val)
    return lst

def Freq(lst,Search):
    Freq = lst[0]
    i = 0
    for val in lst:
        if(Search == val):
            i = i + 1
    return i
    
def main():
    No = int(input("Enter No of elements : "))
    print("Enter the numbers : ")
    
    Res = List(No)
    print("List is ",Res)

    Search = int(input("Element to search : "))

    print("Frequency is : ",Freq(Res,Search))
    
    
if __name__ == "__main__":
    main()