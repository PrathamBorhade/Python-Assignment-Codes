def main():
    list = []
    Max = 0
    No = int(input("Enter No of elements : "))

    print("Enter the numbers : ")

    for i in range(No):
        Val = int(input())
        list.append(Val)
        if(Max < Val):
            Max = Val
        
    print(list)
    print("Maximum element is : ",Max)
    
if __name__ == "__main__":
    main()