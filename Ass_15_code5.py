from functools import reduce
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
    
    Ret = reduce(lambda No1,No2 : No1 if No1 > No2 else No2,Data)

    print("Maximum is : ",Ret)
    
if __name__ == "__main__":
    main()