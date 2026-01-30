import threading

lock = threading.Lock()

def ChkPrime(No):
    for i in range(2,No):
        if(No%i==0):
            return False
    return True

def Prime(lst):
    with lock:
        Data = []
        print("Prime Elements are : ")
        for i in (lst):
            if(ChkPrime(i)):
                Data.append(i)
        print(Data)
        
def NonPrime(lst):
    with lock:
        Data = []
        sum = 0
        print("Non Prime Elements are : ")
        for i in (lst):
            if(ChkPrime(i) == False):
                Data.append(i)
        print(Data)

def main():
    lst = [2,3,4,5,6,7,8,9,10,11,12]
    
    t1 = threading.Thread(target=Prime,args=(lst,))
    t2 = threading.Thread(target=NonPrime,args=(lst,))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()