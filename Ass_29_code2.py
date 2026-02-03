import os
import sys

def FileDisplay(FileName):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} does not exists !")

    fobj = open(FileName,"r")

    Data = fobj.read(100)

    print(f"Data from File is : \n{Data}\n")

    fobj.close()

def main():
    Border = "-"*57
    print(Border)
    print("-------------Marvellous FileDisplay-------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Name ")
        return

    FileDisplay(sys.argv[1])

    print(Border)
    print("---------------END OF APPLICATION----------------")
    print(Border)

if __name__ == "__main__":
    main()