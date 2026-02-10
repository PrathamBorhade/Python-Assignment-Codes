import sys 
import os
from pathlib import Path

def DirectoryExtention(DirectoryName,Extension):
    Border = "-"*57

    fobj = open("Marvellous.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is a Log File created by Marvellous Automation\n")
    fobj.write(Border+"\n")
    
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print(f"{DirectoryName} does not exists")
        return 
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a Directory !")
        return

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:
            filepath = Path(fname)

            if(filepath.suffix == Extension):
                fobj.write("\n\tFile Name : "+fname)

    fobj.write("\n\n"+Border)
    fobj.write("\n"+Border)


def main():
    Border = "-"*57
    print(Border)
    print("-------------Marvellous Directory Extension--------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Inavlid Number of Arguments ")
        print("Please Specify the name of Directory")
        return 

    DirectoryExtention(sys.argv[1],sys.argv[2])

    print(Border)
    print("-------------Marvellous Directory Automation-------------")
    print(Border)


if __name__ == "__main__":
    main()