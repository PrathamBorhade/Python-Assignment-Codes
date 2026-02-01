class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter Name of the Account Holder : ")
        self.Amount = float(input(f"Enter Account Balance : "))

    def Deposit(self):
        self.Damount= float(input("Enter the Amount to Deposit : "))
        self.Amount = self.Amount + self.Damount
        print("Amount Deposited succesfully")
        print(f"Account Balance is : {self.Amount}")


    def Withdraw(self):
        self.Wamount = float(input("Enter the Amount to Deposit : "))
        if(self.Amount < self.Wamount):
            print(f"Insufficient Balance,  Current Balance is : {self.Amount}") 
        else:
            self.Amount = self.Amount - self.Wamount
            print("Withraw Amount succesfully")
            print(f"Account Balance is : {self.Amount}")
        
    def Display(self):
        print(f"The Account Holder Name : {self.Name}")
        print(f"Current Balance is : {self.Amount}")

    def CalculateInterest(self):
        self.interest = 0.0
        self.interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest is : ",self.interest)

while(True):
    print("1] Open Application")
    print("2] Close Application")
    Choice = int(input("Enter Your Choice : "))

    if(Choice == 1):
        
        print("Opening Application")
        obj1 = BankAccount()
        while(True):
            print("-"*22 ,"Menu", "-"*22)
            print("1. Display ")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Calculate Interest")
            print("5. Exit Application")

            print("-"*50)

            Choice = int(input("Enter your choice : "))
            if(Choice == 1):
                obj1.Display()
            elif(Choice == 2):
                obj1.Deposit()
            elif(Choice == 3):
                obj1.Withdraw()
            elif(Choice == 4):
                obj1.CalculateInterest()
            elif(Choice == 5):
                print("Thank You For Using The Application !")
                print("Exiting the Application...")
                print("-"*50)
                break
    elif(Choice == 2):
        print("Closing the Application")
        break
    break

print("-"*50)

while(True):
    print("1] Open Application 2")
    print("2] Close Application 2")
    Choice = int(input("Enter Your Choice : "))

    if(Choice == 1):
        print("Opening Application 2")
        obj2 = BankAccount()
        while(True):
            print("-"*22 ,"Menu", "-"*22)
            print("1. Display ")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Calculate Interest")
            print("5. Exit Application")

            print("-"*50)

            Choice = int(input("Enter your choice : "))
            if(Choice == 1):
                obj2.Display()
            elif(Choice == 2):
                obj2.Deposit()
            elif(Choice == 3):
                obj2.Withdraw()
            elif(Choice == 4):
                obj2.CalculateInterest()
            elif(Choice == 5):
                print("Thank You For Using The Application 2 !")
                print("Exiting the Application 2...")
                break
    elif(Choice == 2):
        print("Closing the Application 2 ")
        break
    break