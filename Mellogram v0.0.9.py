import time
import tempfile
import os


#Standard password
passwordAdmin = "Admin"

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
    
storage = "/"

#Standard parameters
nip = float(0.00000000)
MF = float(0.00000001)
bn = 7
n = 5
nMon = 0
kod = " "

#Secondary functions
Apple = "hor"
Sumsung = "hor"
Microsoft = "hor"

def jojo():
    #Emptiness
    print("\033[H\033[J")
    
def tim():
    #Animation
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

def ast():
    #Apple
    global nip, bn, n, MF
    nip -= MF
    bn = 5
    n = float(0.00000001)

def ast2():
    #Sumsung
    global nip, bn, n, MF
    nip -= MF
    bn = 3
    n = float(0.00000001)

def ast3():
    #Microsoft
    global nip, bn, n, MF
    nip -= MF
    bn = 1
    n = float(0.00000001)

def god():
    #Money +
    global nip
    nip += float(1.00000000)
    jojo()
    dog = input("Your account has been replenished \n>")

def speed():
    #Parameters +
    global bn, n
    bn = 0.1
    n = float(1.00000000)
    jojo()
    dog = input("Your stats have been updated \n>")

   
def setting():
    global kod, storage
    print("Here you will find what you need, I propose to change the rules.")
    print("Kode: "+kod)
    print("Storage: "+storage)
    kodin = input("> ")
    if kodin == "God":
        kod = "God"
        god()
        jojo()
        setting()
    elif kodin == "Speed":
        kod = "Speed"
        speed()
        jojo()
        setting()
    elif kodin == "Storage" or kodin == "storage":
        jojo()
        loop = input("Write a directory where game data can be stored \n> ")
        isDirectory = os.path.isdir(loop)
        if isDirectory == False:
            dog = input("This path does not exist \n> ")
            jojo()
            setting()
        else:
            jojo()
            dog = input("Great, your directory has been saved. \n> ")
            storage = loop
            jojo()
            setting()
    else:
        jojo()
        main()

infgo = "Sumsung"

def login():
    jojo()
    dog = input("Login is not available at the moment \n⋗ ")
    jojo()
    main()
    
        
def registeor():
    global infgo
    jojo()
    dog = input("Registration is not available at the moment \n⋗ ")
    jojo()
    main()
    # hort = input("If you have already created an account, it will be overwritten [Yes/No]")
    # if hort == "Yes":
    #     f = open("Cache.txt", "w")
    #     f.write(infgo)
    #     f.close()
    #     jojo()
    #     dog = input("Great, you are registered. \n⋗ ")
    #     jojo()
    #     ing()
    # elif hort == "No":
    #     jojo()
    #     ing()

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
            ing()
    if lol == 2:
        login()
    elif lol == 1:
        registeor()
    elif lol == 3:
        jojo()
        main()
    else:
        jojo()
        ing()
    
def jkl():
    jog = input("(Yes/No)New password: ")
    if jog == "Yes":
        jojo()
        bog = input("New Password: ")
        if bog == "" or bog == " ":
            print("Password cannot be empty!")
            jojo()
            jkl()
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

#Price per unit
MachineBuy = 0.00039000
PassportBuy = 0.00007000
MachineSell = 0.00019700
PassportSell = 0.00003900

def Shop():
    global nip, MachineBuy, PassportBuy, MachineSell, PassportSell
    print("I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3")
    #Full price per unit
    MachineBuy2 = toFixed(MachineBuy, 8)
    PassportBuy2 = toFixed(PassportBuy, 8)
    MachineSell2 = toFixed(MachineSell, 8)
    PassportSell2 = toFixed(PassportSell, 8)
    #Quantity
    Machine = 12
    Passport = 34
    #Purchase Request
    print("[ 1 ]Machine ("+str(Machine)+"/50) \n[Buy: "+str(MachineBuy2)+"$] \n[Sell: "+str(MachineSell2)+"$]\n\n[ 2 ]Passport ("+str(Passport)+"/200) \n[Buy: "+str(PassportBuy2)+"$] \n[Sell: "+str(PassportSell2)+"$]\n")
    while True:
        try:
            mnb = int(input("Select Item: ")) #Product selection
            break
        except ValueError:
            jojo()
            Shop()
    if mnb == 3:
        jojo()
        main()
    while True:
        try:
            jkp = str(input("Buy or Sell: ")) #Choice of buying and selling
            break
        except ValueError:
            jojo()
            Shop()
    if mnb ==  1 and jkp == "Buy":
        while True:
            try:
                QuantityBuy = int(input("Select Quantity: "))
                break
            except ValueError:
                jojo()
                Shop()
         #Request for the number of things to buy
        if Machine != 0 and nip >= MachineBuy:
            Machine -= QuantityBuy #Subtracting what you need from what you have
            nMon -= (MachineBuy * QuantityBuy) #Subtracting a dollar amount
            InventoryItemMachine = 1 #Purchase ID
            InventoryQuantityMachine = QuantityBuy #Number of items purchased
        else:
            jojo()
            print("You do not have enough money or you do not have the necessary material in storage")
            dog = input("⋗ ")
            jojo()
            Shop()
    # elif mnb == 2 and jkp == "Sell":
    #     QuantityBuy = input("Select Quantity: ")
    else:
        jojo()
        Shop()

def Inventory():
    global InventoryItemMachine
    if InventoryItemMachine == 1:
        print("Machine: "+str(InventoryQuantityMachine))
    else:
        print("Machine: 0")

def main():
    global passwordAdmin
    print("Hello, well, I think you know me, but that doesn't stop us from talking \n[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Shop \n[ 4 ] - Settings \n[ 5 ] - Exit")
    while True:
        try:
            answer = int(input("⋗ "))
            break
        except ValueError:
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
        Shop()
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
    print("Hello, mountain, today we will mine. \n[ 1 ] Mine - start mining \n[ 2 ] Company - select a mining company \n[ 3 ] County - collected money \n[ 4 ] Wallet - crypto details \n[ 5 ] exit - go back ")
    mone()
    
def Wallet():
    global nMon
    while True:
        try:
            vin = int(input("Here you can choose the desired currency, exchange or sell it. \n[ 1 ] Exchanger \n[ 2 ] Exchange Rates \n[ 3 ] Buying a ban \n[ 4 ] exit \n⋗ "))
            break
        except ValueError:
            jojo()
            Wallet()
    if vin == 1:
        jojo()
        Wallet()
    elif vin == 2:
        jojo()
        bot = input("Bitcoin: \nBuy: 100$ = 0.00000236 \n\nSell: 100$ = 0.00000138 \n\n[Buy or Sell]\n⋗ ")
        if bot == "Buy":
            if nMon == 100:
                nMon -= 100
                nip += 0.00000138
                jojo()
                Wallet()
            else:
                jojo()
                dog = input("We did not find the required amount in your account \n> ")
                jojo()
                Wallet()
        elif bot == "Sell":
            if nip >= 0.00000236:
                nip -= 0.00000236
                nMon += 100
            else:
                jojo()
                dog = input("We did not find the required amount in your account \n> ")
                jojo()
                Wallet()
        else:
            jojo()
            dog = input("Please enter buy or sell next time\n> ")
            jojo()
            Wallet()
    elif vin == 4:
        jojo()
        killop()
    else:
        jojo()
        Wallet()

def bartter():
    dog = input("info")
    contract = input("[ 1 ] Apple \n[ 2 ] Sumsung \n [ 3 ] Tesla")

#Mining
def mone():
    global nip, Apple, Sumsung, Microsoft, MF, bn, n
    while True:
        try:
            popi = int(input("⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
            jojo()
            mone()
    if popi == 1:
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
        mineMoney = float(0.00000001)
        if pop == 1:
            tim()
            nip += mineMoney
        elif pop == 2:
            nip += mineMoney*2
            bn = bn*2
            str(tim())*2
            bn = bn/2
        elif pop == 3:
            nip += mineMoney*3
            bn = bn*3
            str(tim())*3
            bn = bn/3
        elif pop == 4:
            nip += mineMoney*4
            bn = bn*4
            str(tim())*4
            bn = bn/4
        elif pop == 5:
            nip += mineMoney*5
            bn = bn*5
            str(tim())*5
            bn = bn/5
        else:
            jojo()
            killop()
            mone()
        nip2 = toFixed(nip, 8)
        print(f'Bitcoin: ' + str(nip2))
        time.sleep(1)
        jojo()
        killop()
    #Companies
    elif popi == 2:
        jojo()
        while True:
            try:
                MF2 = toFixed(MF, 8)
                nip2 = toFixed(nip, 8)
                biy = int(input("[ 1 ] Apple ("+str(nip2)+"/"+str(MF2)+") \n[ 2 ] Sumsung ("+str(nip2)+"/"+str(MF2)+") \n[ 3 ] Microsoft ("+str(nip2)+"/"+str(MF2)+") \n⋗ "))
                break
            except ValueError:
                jojo()
                dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
                jojo()
                mone()
        time.sleep(1)
        if biy == 1:
            if nip >= MF and Apple == "hor":
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
        elif biy == 2:
            if nip >= MF and Sumsung == "hor":
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
        elif biy == 3:
            if nip >= MF and Microsoft == "hor":
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
    elif popi == 3:
        nip2 = toFixed(nip, 8)
        print(f'Bitcoin: ' + str(nip2))
        time.sleep(1)
        jojo()
        killop()
    #exit from window 2
    elif popi == 5:
        jojo()
        main()
    elif popi == 4:
        jojo()
        Wallet()
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
    if bit == 'Yes' or bit == 'yes' or bit == 'y':
        exit()
    elif bit == 'No' or bit == 'no' or bit == 'n':
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
    elif admin == "exit" or admin == "Exit":
        jojo()
        main()
    else:
        Admin()

if __name__ == "__main__":
    main()