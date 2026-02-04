import os
import sys

def FileCopy(FileName1,FileName2):
    Ret = False
    Ret = os.path.exists(FileName1)
    if(Ret == False):
        print(f"{FileName1} does not exists !")
    
    fobj = open(FileName1,"r")

    Data = fobj.read(100)

    fobj2 = open(FileName2,"w")

    fobj2.write(Data)

    print(f"\t Data Copied from {FileName1} to {FileName2}")

    fobj.close()
    fobj2.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("---------------- Marvellous Copy File -------------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid Number Of Arguments !")
        print("Please Specify File Name ")
        return

    FileCopy(sys.argv[1],sys.argv[2])

    print(Border)
    print("------------------ END OF APPLICATION -------------------")
    print(Border)

if __name__ == "__main__":
    main()