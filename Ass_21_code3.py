import threading

iVal = 0
lock = threading.Lock()

def Update():
    global iVal

    for _ in range(20):
        with lock:
            iVal = iVal + 1
            
def main():
    global iVal
    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)
    t3 = threading.Thread(target=Update)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

    print("Value of iVal is : ",iVal)

if __name__ == "__main__":
    main()