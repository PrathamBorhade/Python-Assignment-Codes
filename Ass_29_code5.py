import os
import sys

def FileStringFreq(FileName,string):
    Ret = False
    Ret = os.path.exists(FileName)
    if(Ret == False):
        print(f"{FileName} does not exists !")

    fobj = open(FileName,"r")
    Data = fobj.read(100)

    print(f"Data is : {Data}")

    Count = Data.count(string)

    print(f"{string} appears : {Count} times ")

    fobj.close()
    
def main():
    Border = "-"*57
    print(Border)
    print("-------------- Marvellous String Frequency ---------------")
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