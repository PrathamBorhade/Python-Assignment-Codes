import hashlib
import sys
import os
import time

def DisplayChksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryScanner(Directoryname):
    Border = "-"*57
    
    timestamp = time.strftime("%Y-%m-%d__%H-%M-%S")
    Filename = "ChkSum" + timestamp + ".log"
    fobj = open(Filename,"w")

    fobj.write(Border + "\n")
    fobj.write("----------------- Marvellous Checksum  ------------------\n")
    fobj.write(f"---------- Log created at : {timestamp} --------\n")
    fobj.write(Border+"\n")

    Res = False

    Res = os.path.exists(Directoryname)
    if(Res == False):
        print("Invalid Directory does not exist\n")
        return 

    Res = os.path.isdir(Directoryname)
    if(Res == False):
        fprint("Invalid Give name of a directory\n")
        return 

    fobj.write("\t\t\t\t\tCheckSum Report \n\n")

    for FolderName , SubFolderName, FileName in os.walk(Directoryname):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = DisplayChksum(fname)

            fobj.write(f"File Name : {fname} | Check sum : {Checksum}\n")

    print("\n Log reported Generated \n")

    fobj.write(Border+"\n")
    fobj.write("------------------ Marvellous Checksum  -----------------\n")
    fobj.write(Border+"\n")

def main():
    Border = "-"*57
    print(Border)
    print("----------------- Marvellous Checksum  ------------------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Inavlid Number of Arguments ")
        print("Please Specify the name of Directory")
        return 

    DirectoryScanner(sys.argv[1])

    print(Border)
    print("----------------- Marvellous Checksum -------------------")
    print(Border)    

if __name__ == "__main__":
    main()