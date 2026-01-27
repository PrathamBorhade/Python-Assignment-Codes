def main():
    list = []
    Sum = 0
    No = int(input("Enter No of elements : "))

    print("Enter the numbers : ")

    for i in range(No):
        Val = int(input())
        list.append(Val)
        Sum += Val

    print(list)
    print("Addition of all elements is : ",Sum)
    
if __name__ == "__main__":
    main()