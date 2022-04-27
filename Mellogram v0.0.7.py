import time


#import datetime
#x = datetime.datetime.now()
#timeS = str(x.strftime("%X"))
#"[" + timeS + "]" + 

#Standard storage and password
defaultCesh = "/storage/emulated/0/Download/"
passwordAdmin = "Admin"

#Standard parameters
nip = 0
bn = 7
n = 5

#Secondary functions
Apple = "hor"
Sumsung = "hor"
Microsoft = "hor"

def jojo():
    #Emptiness
    print("\033[H\033[J")
    
def tim():
    #Animation
    global nip
    jojo()
    print("0%[••••••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("5%[#•••••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("10%[##•••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("15%[###••••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("21%[####•••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("26%[#####••••••••••••••]")
    time.sleep(bn)
    jojo()
    print("31%[######•••••••••••••]")
    time.sleep(bn)
    jojo()
    print("36%[#######••••••••••••]")
    time.sleep(bn)
    jojo()
    print("42%[########•••••••••••]")
    time.sleep(bn)
    jojo()
    print("47%[#########••••••••••]")
    time.sleep(bn)
    jojo()
    print("52%[##########•••••••••]")
    time.sleep(bn)
    jojo()
    print("57%[###########••••••••]")
    time.sleep(bn)
    jojo()
    print("63%[############•••••••]")
    time.sleep(bn)
    jojo()
    print("68%[#############••••••]")
    time.sleep(bn)
    jojo()
    print("73%[##############•••••]")
    time.sleep(bn)
    jojo()
    print("78%[###############••••]")
    time.sleep(bn)
    jojo()
    print("84%[################•••]")
    time.sleep(bn)
    jojo()
    print("89%[#################••]")
    time.sleep(bn)
    jojo()
    print("94%[##################•]")
    time.sleep(bn)
    jojo()
    print("100%[##################]")
    time.sleep(bn)
    jojo()
    nip += n

def ast():
    #Apple
    global nip, bn, n
    nip -= 100
    bn = 5
    n = 50

def ast2():
    #Sumsung
    global nip, bn, n
    nip -= 45
    bn = 3
    n = 30

def ast3():
    #Microsoft
    global nip, bn, n
    nip -= 23
    bn = 1
    n = 10

def god():
    #Money +
    global nip
    nip += 1000

def speed():
    #Parameters +
    global bn, n
    bn = 0.1
    n = 1000
   
def setting():
    print("Here you will find what you need, I propose to change the rules.")
    kode = str(input("Kode: "))
    vbn = str(input("Storage: "))
    #Increased score
    if kode == "God":
        god()
        dog = input("Well good, your account is replenished with 1000 coins \n> ")
        jojo()
        main()
    #Increase parameters
    elif kode == "Speed":
        speed()
        dog = input("Well good, your parameters are increased \n> ")
        jojo()
        main()
    else:
        dog = input("Error kodes \n> ")
        jojo()
        main()
    if vbn == None:
        dog = input("Please specify the address \n> ")
    else:
        defaultCesh = vbn
    
def login():
    pass
    
def ing():
    jojo()
    while True:
        try:
            lol = int(input("To save or create an entry, you need to create an account \n[ 1 ] Register \n[ 2 ] Login \n[ 3 ] exit \n⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  You have blocked access to the storage!  Try again... \n⋗ ")
            jojo()
    if lol == 2:
        login()
    elif lol == 1:
        jojo()
        UserFname = str(input("Your First name: "))
        UserLname = str(input("Your Last name: "))
        UserPass = str(input("Your Password: "))
        while True:
            try:
                f = open(defaultCash + UserFname + ' ' + UserLname + ".txt", "a")
                break
            except PermissionError:
                jojo()
                dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
                jojo()
                ing()
        f.write("First Name = " + UserFname + '\n' + "Last Name = " + UserLname + '\n' + "Password = " + UserPass)
        f.close()
    elif lol == 3:
        jojo()
        main()
    else:
        jojo()
        dog = input("Unknown error \n⋗ ")
        jojo()
        ing()
    
def jkl():
    jog = input("(Yes/No)New password: ")
    if jog == "Yes":
        jojo()
        bog = input("New Password: ")
        if bog == "" or bog == " ":
            print("Password cannot be empty!")
        else:
            passwordAdmin = bog
            jojo()
            Admin()
    elif jog == "No":
        jojo()
        Admin()
    else:
        jojo()
        main()

def main():
    global passwordAdmin
    print("Hello, well, I think you know me, but that doesn't stop us from talking \n[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Shop \n[ 4 ] - Settings \n[ 5 ] - Exit")
    while True:
        try:
            answer = int(input("⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
            jojo()
            main()
    #Start the game
    if answer == 1:
        killop()
        jojo()
    #Continue game
    elif answer == 2:
        ing()
    #Score
    elif answer == 3:
        jojo()
        print("Under development")
        dog = input("⋗ ")
        jojo()
        main()
    #Settings
    elif answer == 4:
        jojo()
        setting()
    #Output
    elif answer == 5:
        jojo()
        hopy()
    elif answer == 6:
        jojo()
        hog = input("Password: ")
        if hog == passwordAdmin:
            jojo()
            jkl()
        else:
            jojo()
            main()
            
    else:
        jojo()
        main()

#Window #2
def killop():
    jojo()
    print("Hello, mountain, today we will mine. \n/Mine - start mining \n/Company - select a mining company \n/County - collected money \n/exit - go back ")
    mone()

#Mining
def mone():
    global nip, Apple, Sumsung, Microsoft
    while True:
        try:
            popi = str(input("⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
            jojo()
            mone()
    if popi == "/Mine" or popi == "/mine":
        jojo()
        while True:
            try:
                pop = int(input("How many farms do you want to run?(0/5) \n⋗ "))
                break
            except ValueError:
                jojo()
                dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
                jojo()
                killop()
        #Farm
        if pop == 1:
            tim()
        elif pop == 2:
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 3:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 4:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        elif pop == 5:
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
            time.sleep(0.5)
            tim()
        else:
            jojo()
            killop()
            mone()
        print(f'Money' + ' ' + str(nip))
        time.sleep(1)
        jojo()
        killop()
    #Companies
    elif popi == "/Company" or popi == "/company":
        jojo()
        while True:
            try:
                biy = int(input("[ 1 ] Apple ("+str(nip)+"/100) \n[ 2 ] Sumsung ("+str(nip)+"/45) \n[ 3 ] Microsoft ("+str(nip)+"/23) \n⋗ "))
                break
            except ValueError:
                jojo()
                dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
                jojo()
                mone()
        time.sleep(1)
        if biy == 1:
            if nip >= int(100) and Apple == "hor":
                ast()
                jojo()
                print("Your money was transferred to the company")
                Apple = "horo"
                dog = input("⋗ ")
                jojo()
                killop()
            else:
                jojo()
                print("You have less than the required amount, or you already have assets of this company")
                dog = input("⋗ ")
                jojo()
                killop()
            #Samsung
            if biy == 2:
                if kit >= int(45) and Sumsung == "hor":
                    ast2()
                    jojo()
                    print("Your money was transferred to the company")
                    Sumsung = "horo"
                    dog = input("⋗ ")
                    jojo()
                    killop()
                else:
                    jojo()
                    print("You have less than the required amount")
                    dog = input("⋗ ")
                    jojo()
                    killop()
            if biy == 3:
                if kit >= int(23) and Microsoft == "hor":
                    ast3()
                    jojo()
                    print("Your money was transferred to the company")
                    Microsoft = "horo"
                    dog = input("⋗ ")
                    jojo()
                    killop()
                else:
                    jojo()
                    print("You have less than the required amount, or you already have assets of this company")
                    time.sleep(1)
                    jojo()
                    killop()
        else:
            jojo()
            killop()
    #Money
    elif popi == "/County" or popi == "/county":
        print(f'Money' + ' ' + str(nip))
        time.sleep(1)
        jojo()
        killop()
    #exit from window 2
    elif popi == "/exit" or popi == "/Exit":
        jojo()
        main()
    else:
        print("Unknown error")
        jojo()
        killop()

#Game Exit Confirmation
def hopy():
    while True:
        try:
            bit = str(input("Exit? \n[ Yes ] [ No ] \n⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
            jojo()
            hopy()
    if bit == 'Yes' or bit == 'yes':
        exit()
    elif bit == 'No' or bit == 'no':
        jojo()
        main()
    else:
        print("Unknown error")
        jojo()
        main()


def Admin():
    admin = input("> ")
    if admin == "jojo()":
        jojo()
        print("Complete")
        Admin()
    elif admin == "tim()":
        tim()
        print("Complete")
        Admin()
    elif admin == "ast()":
        ast()
        print("Complete")
        Admin()
    elif admin == "ast2()":
        ast2()
        print("Complete")
        Admin()
    elif admin == "ast3()":
        ast3()
        print("Complete")
        Admin()
    elif admin == "god()":
        god()
        print("Complete")
        Admin()
    elif admin == "speed()":
        speed()
        print("Complete")
        Admin()
    elif admin == "setting()":
        setting()
        print("Complete")
        Admin()
    elif admin == "main()":
        main()
        print("Complete")
        Admin()
    elif admin == "login()":
        login()
        print("Complete")
        Admin()
    elif admin == "ing()":
        ing()
        print("Complete")
        Admin()
    elif admin == "hopy()":
        hopy()
        print("Complete")
        Admin()
    elif admin == "mone()":
        mone()
        print("Complete")
        Admin()
    elif admin == "killop()":
        killop()
        print("Complete")
        Admin()
    elif admin == "help":
        print("""
1 jojo()
2 tim()
3 ast()
4 ast2()
5 ast3()
6 god()
7 speed()
8 setting()
9 main()
10 login()
11 ing()
12 hopy()
13 mone()
14 killop()
15 help
16 exit""")
        Admin()
    elif admin == "exit":
        main()
        Admin()
    else:
        Admin()

if __name__ == "__main__":
    main()