import threading

lock = threading.Lock()

def Small(lst):
    with lock:
        Data = []
        for i in lst:
            string = str(i)
            if string.islower():
                Data.append(string)

        print("Lowercase are : ",Data)

def Capital(lst):
    with lock:        
        Data = []
        for i in lst:
            string = str(i)
            if string.isupper():
                Data.append(string)

        print("Uppercase are : ",Data)

def Digits(lst):
    with lock:        
        Data = []
        for i in lst:
            string = str(i)
            if string.isnumeric():
                Data.append(string)

        print("Numeric Digits are : ",Data)

def main():
    lst = "String 123"

    t1 = threading.Thread(target=Small,args=(lst,))
    t2 = threading.Thread(target=Capital,args=(lst,))    
    t3 = threading.Thread(target=Digits,args=(lst,))    

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()