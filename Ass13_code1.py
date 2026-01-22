def AreaRectangle(No1,No2):
    Area = No1 * No2
    return  Area

def main():
    len = int(input("Enter length of the reactangle : "))
    Wid = int(input("Enter width of the reactangle : "))
    Ret = AreaRectangle(len,Wid)

    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()