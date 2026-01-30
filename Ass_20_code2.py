import threading

lock = threading.Lock()

def EvenFactor(No):
    
    with lock:
        Fact = []
        sum = 0
        print("Even Factors are : ")
        for i in range(1,No+1):
            if(No%i==0):
                Fact.append(i)
                if(i%2==0):
                    sum = sum + i
        print(Fact)
        print("Sum is : ",sum)

def OddFactor(No):
    with lock:
        Fact = []
        sum = 0
        print("Odd Factors are : ")
        for i in range(1,No+1):
            if(No%i==0):
                Fact.append(i)
                if(i%2!=0):
                    sum = sum + i
        print(Fact)
        print("Sum is : ",sum)

def main():
    No = int(input(print("Enter a No")))

    t1 = threading.Thread(target=EvenFactor,args=(20,))
    t2 = threading.Thread(target=OddFactor,args=(20,))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()