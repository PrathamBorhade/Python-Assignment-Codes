def Grade(No):
    if(No >= 75):
        return 1
    elif(No >= 60):
        return 2
    elif(No >= 50):
        return 3
    else:
        return 4

def main():
    No = int(input("Enter a No : "))
    Ret = Grade(No)

    if(Ret == 1):
        print("Grade : Disticntion")
    elif(Ret == 2):
        print("Grade : First Class")
    elif(Ret == 3):
        print("Grade : Second Class")
    elif(Ret == 4):
        print("Fail")

if __name__ == "__main__":
    main()