def ChkVowel(Ch):
    if(Ch =="a" or Ch =="e" or Ch =="i" or Ch =="o" or Ch =="u"):
        return True
    else:
        return False

def main():
    Ch = input("Enter a alpabhet : ")
    Ret = ChkVowel(Ch)

    if(Ret == True):
        print("It is a vowel")
    else:
        print("Not a vowel")

if __name__ == "__main__":
    main()