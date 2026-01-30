import threading

lock = threading.Lock()

def EvenList(lst):
    with lock:
        Even = []
        sum = 0
        print("Even Elements are : ")
        for i in (lst):
            if(i%2==0):
                Even.append(i)
                sum = sum + i
        print(Even)
        print("Sum is : ",sum)

def OddList(lst):
    with lock:
        Odd = []
        sum = 0
        print("Odd Factors are : ")
        for i in (lst):
                if(i%2!=0):
                    Odd.append(i)
                    sum = sum + i
        print(Odd)
        print("Sum is : ",sum)

def main():
    No = int(input("Enter No of elements : "))
    print("Enter the numbers : ")
    
    lst = []
    
    for i in range(No):
        Val = int(input())
        lst.append(Val)

    print("List is ",lst)

    t1 = threading.Thread(target=EvenList,args=(lst,))
    t2 = threading.Thread(target=OddList,args=(lst,))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()