def AreaCircle(r):
    pi = 3.12
    Area = pi*r**2
    return  Area

def main():
    Rad = int(input("Enter Radius of Circle : "))
    Ret = AreaCircle(Rad)

    print("Area of Circle is ~ ",Ret)

if __name__ == "__main__":
    main()