import threading

lock = threading.Lock()

def Sum(lst,Res):
    with lock:
        sum = 0
        for i in (lst):
           sum += i
        Res[0] = sum
        return Res[0] 


def Product(lst,Res):
    with lock:
        Prod = 1    
        for i in (lst):
            Prod = Prod * i
        Res[1] = Prod
        return Res[1]

def main():
    lst = [2,3,4,5,6,7,1,8,9,10,11,12]
    print("List of elements : ",lst)

    Res = [None,None]
    
    t1 = threading.Thread(target=Sum,args=(lst,Res))
    t2 = threading.Thread(target=Product,args=(lst,Res))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
    print("Summation is : ",Res[0])
    print("Product is : ",Res[1])


if __name__ == "__main__":
    main()