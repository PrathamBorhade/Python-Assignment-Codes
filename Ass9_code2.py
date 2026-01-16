def ChkGreater(no1,no2):
    if(no1 > no2):
        return no1
    else:
        return no2

print("Enter first no : ")
No1 = int(input())

print("Enter second no : ")
No2 = int(input())

Result = ChkGreater(No1,No2)
print("Greater is : ",Result)