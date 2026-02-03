import os
import sys

def FileCompare(FileName1,FileName2):
    Ret = False
    Ret = os.path.exists(FileName1)
    if(Ret == False):
        print(f"{FileName1} does not exists !")

    Ret = os.path.exists(FileName2)
    if(Ret == False):
        print(f"{FileName2} does not exists !")

    fobj = open(FileName1,"r")
    Data1 = fobj.read(100)

    fobj2 = open(FileName2,"r")
    Data2 = fobj2.read(100)

    if(Data1 == Data2):
        print("\nSuccess")
        print(f"{FileName1} and {FileName2} contains same content \n")
    else:
        print("\nFailure")
        print(f"{FileName1} and {FileName2} does not contain same content \n")

    fobj.close()
    fobj2.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("---------------- Marvellous File Compare ----------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Names ")
        return

    FileCompare(sys.argv[1],sys.argv[2])

    print(Border)
    print("------------------ END OF APPLICATION -------------------")
    print(Border)

if __name__ == "__main__":
    main()