import hashlib
import os
import sys
import time

def ChkSum(Filename):
    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DisplayDuplicate(DirectoryName):
    Border = "-"*57
   
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    Filename = "DuplicateDisplay" + timestamp + ".log"
    fobj = open(Filename,"w")
     
    fobj.write(Border+"\n")
    fobj.write("-------------------Marvellous Duplicate-------------------\n")
    fobj.write(f"-----------Log Created at :{timestamp}-----------\n")
    fobj.write(Border+"\n")

    Res = False

    Res = os.path.exists(DirectoryName)
    if(Res == False):
        fobj.write("The Directory Does Not Exist\n")
        return
    
    fobj.write("\t \t \t  Duplicate File Report\n")
    fobj.write(Border+"\n")

    
    Res = os.path.isdir(DirectoryName)
    if(Res == False):
        fobj.write("Invalid option not a directory\n")
        return
    
    Duplicate = {}

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            files = os.path.join(FolderName,fname)
            Checksum = ChkSum(files)
            
            if Checksum in Duplicate:
                fobj.write(f"File Name : {files} is duplicate of File : {Duplicate[Checksum]} is from Folder :{FolderName}\n")
            else:
                Duplicate[Checksum] = files

    fobj.write(Border+"\n")
    fobj.write("-------------------Marvellous Duplicate-------------------"+"\n")
    fobj.write(Border+"\n")

    fobj.close()


def main():
    Border = "-"*57
    print(Border)
    print("-------------------Marvellous Duplicate-------------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Inavlid Number of Arguments ")
        print("Please Specify the name of Directory")
        return 

    DisplayDuplicate(sys.argv[1])
    print("Log Report Generated !")

    print(Border)
    print("------------------Marvellous Duplicate--------------------")
    print(Border)

if __name__ == "__main__":
     main()