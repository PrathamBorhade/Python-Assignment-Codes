def binary(No):
    result = bin(No)
    return result

def main():
    No = int(input("Enter a No : "))
    Ret = binary(No)

    print("Binary equivalent is : ",Ret)
    
if __name__ == "__main__":
    main()