Power = lambda No : No**2

def main():
    No = int(input("Enter a No : "))

    Res = Power(No)
    print(f"Power of two of {No} is : ",Res)    
    
if __name__ == "__main__":
    main()        