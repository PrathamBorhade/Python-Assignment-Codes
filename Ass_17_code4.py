def main():
    sum = 0 
    No = int(input("Enter a number : "))
    for i in range(1,No):
        if(No%i==0):
            sum = sum + i
    print(sum)

if __name__ == "__main__":
    main()