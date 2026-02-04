import os
import sys

def FileStringFreq(FileName,string):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} does not exists !")

    fobj = open(FileName,"r")
    Data = fobj.read(100)

    Count = Data.count(string)

    if(Count > 0):
        print(f"\t\t{string} found in {FileName}")
    else:
        print(f"\t\t{string} not found in {FileName}")
    
    fobj.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("---------------- Marvellous Search Word ------------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Name ")
        return

    FileStringFreq(sys.argv[1],sys.argv[2])

    print(Border)
    print("------------------- END OF APPLICATION -------------------")
    print(Border)

if __name__ == "__main__":
    main()