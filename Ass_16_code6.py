def Check(No):
    if(No > 0):
       return True
    elif(No < 0):
        return False

def main():
    No = int(input("Enter a number :"))
    Res = Check(No)

    if(Res == True):
        print("Positive number")
    elif(Res == False):
        print("Negative number")
    else:
        print("Zero")

if __name__ =="__main__":
    main()