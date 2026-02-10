import sys 
import os
import shutil
import time
from pathlib import Path

def DirectoryCopyExt(Source,Destination,Extension):
    Border = "-"*57

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = "Marvellous"+"_"+timestamp+".log" 

    fobj = open(filename,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a Log File created by Marvellous Automation\n")
    fobj.write("Created at : "+time.strftime("%Y-%m-%d__%H:%M:%S")+"\n")
    fobj.write(Border+"\n")
    
    Ret = False
    Ret = os.path.exists(Source)
    
    if(Ret == False):
        print(f"{Source} does not exists")
        fobj.close()
        return 
    
    Ret = os.path.isdir(Source)

    if(Ret == False):
        print("It is not a Directory !")
        fobj.close()
        return

    os.makedirs(Destination, exist_ok=True)
    fobj.write(f"Created Destination Directory : {Destination}\n")
    fobj.write(Border+"\n")

    for FolderName,SubFolderName,FileName in os.walk(Source):
        for file in FileName:
            src_path = os.path.join(FolderName,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            filepath = Path(file)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            if(not os.path.exists(dest_path)):
                if(filepath.suffix == Extension):
                    shutil.copy2(src_path,dest_path)
                    fobj.write(f"{file} Copied succesfully to {Destination} from {Source}\n")
                else:
                    return
            else:
                fobj.write("Unable to Copy as File already exists\n")
                print(f"Unable to copy {Destination} as it already exists")
                return

    print(f"\tFiles Copied Succesfully to {Destination}")

    fobj.write("\n"+Border)
    fobj.write("\n"+Border)
    fobj.close()

def main():
    Border = "-"*57
    print(Border)
    print("--------------- Marvellous Directory Copy ---------------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Inavlid Number of Arguments ")
        print("Please Specify the name of Directory")
        return 

    DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])

    print(Border)
    print("--------------- Marvellous Directory Copy ---------------")
    print(Border)

if __name__ == "__main__":
    main()