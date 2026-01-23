sqaure = lambda No : No**2 

def main():
    size = 0    
    No = 0

    print("Enter no of elements :")
    size = int(input())

    Data = list()
    print("Enter the numbers : ")
    
    for i in range(size):
        No = int(input())
        Data.append(No)
    
    print("list is : ",Data)
    
    Ret = list(map(sqaure,Data))

    print("Sqaure of given no is : ",Ret)
    
if __name__ == "__main__":
    main()