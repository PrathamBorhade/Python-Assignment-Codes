def main():
    size = 0    
    No = 0

    print("Enter no of elements :")
    size = int(input())

    Data = list()
    print("Enter the strings : ")
    
    for i in range(size):
        string = input()
        Data.append(string)
    
    print("list is : ",Data)
    
    Ret = list(filter(lambda string : len(string) > 5,Data))

    print("strings length more than 5 are : ",Ret)
    
if __name__ == "__main__":
    main()