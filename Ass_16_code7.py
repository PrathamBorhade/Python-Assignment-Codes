def Div5(No):
    if(No%5 == 0):
       return True
    else:
        return False

def main():
    No = int(input("Enter a number :"))
    Res = Div5(No)
    print(Res)

if __name__ =="__main__":
    main()