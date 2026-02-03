import os
import sys

def FileScanner(FileName):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == True):
        print(f"{FileName} exists ! ")
    else:
        print(f"{FileName} does not exists !")

def main():
    Border = "-"*57
    print(Border)
    print("-------------Marvellous FileScanner-------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Name ")
        return

    FileScanner(sys.argv[1])

if __name__ == "__main__":
    main()