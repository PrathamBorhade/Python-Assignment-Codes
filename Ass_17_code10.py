def main():
    No = int(input("Enter a number : "))
    sum = 0
    while No > 0:
        sum += No%10
        No //=10 
    
    print("Sum : ",sum)
    
if __name__ == "__main__":
    main()