import threading

lock = threading.Lock()

def Maximum(lst):
    with lock:
        Max = 0
        print("Maximum Element is : ")
        for i in (lst):
            if i > Max:
                Max = i
            
        print(Max)
        
def Minimum(lst):
    with lock:
        Min = lst[0]
        print("Minimum Elements is : ")
        for i in (lst):
            if i < Min:
                Min = i
        print(Min)

def main():
    lst = [2,3,4,5,6,7,1,8,69,9,10,11,12]
    
    t1 = threading.Thread(target=Maximum,args=(lst,))
    t2 = threading.Thread(target=Minimum,args=(lst,))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()