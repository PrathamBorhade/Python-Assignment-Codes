import threading

lock = threading.Lock()

def Thread1():
    with lock:
        Data = []
        print("No in sequence from 1 to 50 : ")
        for i in range(1,51):
            Data.append(i)
        print(Data)

def Thread2():
    with lock:
        Data = []
        print("No in reverse from 50 to 1 : ")
        for i in range(50,0,-1):
            Data.append(i)
        print(Data)
        
def main():

    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
