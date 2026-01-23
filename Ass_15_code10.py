def main():
    size = 0    
    No = 0

    print("Enter no of elements :")
    size = int(input())

    Data = list()
    print("Enter the nos : ")
    
    for i in range(size):
        No = int(input())
        Data.append(No)
    
    print("list is : ",Data)
    
    Ret = list(filter(lambda No : No%2==0,Data))

    print("No of Even numbers are : ",len(Ret))
    
if __name__ == "__main__":
    main()