import os
import sys

def CountLines(FileName):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} does not exists !")

    fobj = open(FileName,"r")
    
    Count = 0

    for lines in fobj:
        Count += 1
    print(f"\t      There are {Count} lines in {FileName}")

    fobj.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("---------------- Marvellous Count Lines -----------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Name ")
        return

    CountLines(sys.argv[1])

    print(Border)
    print("------------------ END OF APPLICATION -------------------")
    print(Border)

if __name__ == "__main__":
    main()