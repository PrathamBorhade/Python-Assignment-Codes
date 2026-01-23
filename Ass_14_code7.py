Odd = lambda No : No%5 == 0 

def main():
    No = int(input("Enter a No : "))
    Ret = Odd(No)
    print(Ret)

if __name__ == "__main__":
    main()