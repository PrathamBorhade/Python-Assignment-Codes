import os
import sys

def CountLines(FileName):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} does not exists !")

    fobj = open(FileName,"r")
    Data = fobj.read(1024)

    Words = Data.split()    

    print(f"\t      There are {len(Words)} Words in {FileName}")

    fobj.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("---------------- Marvellous Count Words -----------------")
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