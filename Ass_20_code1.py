import threading

lock = threading.Lock()

def Even():
    with lock:
        print("First Even no are : ")
        for i in range(2,10+1,2):
            print(i)

def Odd():
    with lock:
        print("First Odd no are : ")
        for i in range(1,10+1,2):
            print(i)

def main():

    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
