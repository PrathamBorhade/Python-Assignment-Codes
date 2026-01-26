def main():
    Fact = 1
    No = int(input("Enter a number : "))
    for i in range(1,No+1):
        Fact = Fact * i

    print(Fact)

if __name__ == "__main__":
    main()