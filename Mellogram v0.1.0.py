import time
import tempfile
import os

#Standard password
passwordAdmin = "Admin"

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#login >> arr = [['1','Марина','1'],['1','Маша','1'],['1','Миша','1']]
#login >> res = [el for el in arr if el[1].startswith("Мар")]
#login >> list = input().split() #Display content as a list

#Standard parameters
nip = float(0.00000000)
bn = 7
n = 5
nMon = 0
kod = " "

storage = "/"

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

MoneyApple = 0.00000100
MoneySumsung = 0.00000045
MoneyMicrosoft = 0.00000026

def ast():
    #Apple
    global nip, bn, n, MoneyApple
    nip -= MoneyApple
    bn = 5
    n = float(0.00000004)

def ast2():
    #Sumsung
    global nip, bn, n, MoneySumsung
    nip -= MoneySumsung
    bn = 3
    n = float(0.00000007)

def ast3():
    #Microsoft
    global nip, bn, n, MoneyMicrosoft
    nip -= MoneyMicrosoft
    bn = 1
    n = float(0.00000012)

def god():
    #Money +
    global nip
    nip += float(1.00000000)

def speed():
    #Parameters +
    global bn, n, nip
    bn = 0.1
    n = float(1.00000000)
   
def setting():
    global kod, storage
    kodin = input("Here you will find what you need, I propose to change the rules. \nKode: "+str(kod)+"\nStorage: "+str(storage)+"\n> ")
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
    elif kodin == "exit":
        jojo()
        main()
    else:
        jojo()
        setting()
    
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
#Quantity
Machine = 12
Passport = 34

InventoryItemMachine = 0
InventoryQuantityMachine = 0
InventoryItePassport = 0
InventoryQuantityPassport = 0

def Shop():
    global InventoryItePassport, InventoryQuantityMachine, nip, MachineBuy, PassportBuy, MachineSell, PassportSell, Machine, Passport, InventoryItemMachine, InventoryQuantityPassport
    print("I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3")
    #Full price per unit
    MachineBuy2 = toFixed(MachineBuy, 8)
    PassportBuy2 = toFixed(PassportBuy, 8)
    MachineSell2 = toFixed(MachineSell, 8)
    PassportSell2 = toFixed(PassportSell, 8)
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
        if Machine > 0 and nip >= MachineBuy:
            Machine -= QuantityBuy
            nip -= MachineBuy * QuantityBuy
            InventoryQuantityMachine += QuantityBuy 
            jojo()
            dog = input("Added a new item to your inventory\n> ")
            jojo()
        else:
            print("You do not have enough money or you do not have the necessary material in storage")
            dog = input("⋗ ")
            jojo()
            Shop()
    elif mnb == 1 and jkp == "Sell":
        while True:
            try:
                QuantitySell = input("Select Quantity: ")
                break
            except ValueError:
                jojo()
                Shop()
        if InventoryQuantityMachine >= QuantitySell and QuantityBuy < Machine:
            Machine += QuantitySell
            nip += MachineSell * QuantitySell
            InventoryItemMachine = 1
            InventoryQuantityMachine -= QuantitySell
        else:
            jojo()
            dog = input("You do not have Machine in inventory \n> ")
            jojo()
            main()
    #Passport
    if mnb ==  2 and jkp == "Buy":
        while True:
            try:
                QuantityBuy = int(input("Select Quantity: "))
                break
            except ValueError:
                jojo()
                Shop()
         #Request for the number of things to buy
        if Passport > 0 and nip >= PassportBuy and QuantityBuy < Passport:
            Passport -= QuantityBuy 
            nip -= PassportBuy * QuantityBuy
            InventoryQuantityPassport += QuantityBuy
        else:
            jojo()
            print("You do not have enough money or you do not have the necessary material in storage")
            dog = input("⋗ ")
            jojo()
            Shop()
    elif mnb == 2 and jkp == "Sell":
        while True:
            try:
                QuantitySell = input("Select Quantity: ")
                break
            except ValueError:
                jojo()
                Shop()
        if InventoryQuantityPassport >= QuantitySell:
            Passport += QuantitySell
            nip += PassportSell * QuantitySell
            InventoryQuantityPassport -= QuantitySell
        else:
            jojo()
            dog = input("You do not have Passport in inventory \n> ")
            jojo()
            Shop()
    else:
        dog = input("#Error#")
        jojo()
        Shop()

def Inventory():
    global InventoryQuantityMachine, InventoryQuantityPassport
    print("We have prepared information about your equipment for you, keep. \nMachine: "+str(InventoryQuantityMachine)+"\n\nPassport: "+str(InventoryQuantityPassport))

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
        jojo()
        killop()
    #Continue game
    elif answer == 2:
        jojo()
        main()
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
    print("Hello, mountain, today we will mine. \n[ 1 ] Mine - start mining \n[ 2 ] Company - select a mining company \n[ 3 ] County - collected money \n[ 4 ] Wallet - crypto details \n[ 5 ] Bartter - available temporary work \n[ 6 ] exit - go back ")
    mone()
    
bitcoinBuy = 0.00000236
bitcoinSell = 0.00000138
bitcoinBuy2 = toFixed(bitcoinBuy, 8)
bitcoinSell2 = toFixed(bitcoinSell, 8)

def Wallet():
    global nMon, nip, bitcoinBuy, bitcoinSell, bitcoinSell2, bitcoinBuy2
    while True:
        try:
            vin = int(input("Here you can choose the desired currency, exchange or sell it. \n[ 1 ] Exchanger \n[ 2 ] Exchange Rates \n[ 3 ] Buying a ban\n[ 5 ] Inventory \n[ 6 ] exit \n⋗ "))
            break
        except ValueError:
            jojo()
            Wallet()
    if vin == 1:
        jojo()
        Wallet()
    elif vin == 2:
        jojo()
        bot = input("Bitcoin: \nBuy: 100$ = "+str(bitcoinBuy2)+" \n\nSell: 100$ = "+str(bitcoinSell2)+" \n\n[Buy or Sell]\n⋗ ")
        if bot == "Buy":
            if nMon >= 100:
                nMon -= 100
                nip += bitcoinBuy
                jojo()
                Wallet()
            else:
                jojo()
                dog = input("We did not find the required amount in your account \n> ")
                jojo()
                Wallet()
        elif bot == "Sell":
            if nip >= bitcoinSell:
                nip -= bitcoinSell
                nMon += int(100)
                jojo()
                Wallet()
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
    elif vin == 5:
        jojo()
        Inventory()
    elif vin == 6:
        jojo()
        killop()
    else:
        jojo()
        Wallet()

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Process...")
        time.sleep(1)
        num_of_secs -= 1

def bartter():
    contract = int(input("A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n\n> "))
    if contract == 1:
        bartter = input("Working conditions \n\nTime: 1:00h \nMoney: 500$ \n[Yes/No]")
        if bartter == "Yes" or bartter == "yes" or bartter == "y" or bartter == "Y":
            bartterConfirmation = input("You are sure? After all, your device will work for the company")
            if bartterConfirmation == "Yes" or bartterConfirmation == "yes" or bartterConfirmation == "y" or bartterConfirmation == "Y":
                timeC = 3600
                print('Countdown finished.')
                inp = timeC
                countdown(int(inp))
                nMon += 500
                jojo()
                killop()
    elif contract == 2:
        bartter = input("Working conditions \n\nTime: 45m \nMoney: 300$ \n[Yes/No]")
        if bartter == "Yes" or bartter == "yes" or bartter == "y" or bartter == "Y":
            bartterConfirmation = input("You are sure? After all, your device will work for the company")
            if bartterConfirmation == "Yes" or bartterConfirmation == "yes" or bartterConfirmation == "y" or bartterConfirmation == "Y":
                timeC = 2700
                inp = timeC
                countdown(int(inp))
                nMon += 300
                jojo()
                killop()
    elif contract == 3:
        bartter = input("Working conditions \n\nTime: 25m \nMoney: 150$ \n[Yes/No]")
        if bartter == "Yes" or bartter == "yes" or bartter == "y" or bartter == "Y":
            bartterConfirmation = input("You are sure? After all, your device will work for the company")
            if bartterConfirmation == "Yes" or bartterConfirmation == "yes" or bartterConfirmation == "y" or bartterConfirmation == "Y":
                timeC = 1500
                inp = timeC
                countdown(int(inp))
                nMon += 150
                jojo()
                killop()
    else:
        jojo()
        killop()

#Mining
def mone():
    global nip, MoneySumsung, MoneyApple, MoneyMicrosoft, Apple, Sumsung, Microsoft, MF, bn, n
    while True:
        try:
            popi = int(input("⋗ "))
            break
        except ValueError:
            jojo()
            dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
            jojo()
            killop()
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
                MoneyApple2 = toFixed(MoneyApple, 8)
                MoneySumsung2 = toFixed(MoneySumsung, 8)
                MoneyMicrosoft2 = toFixed(MoneyMicrosoft, 8)
                nip2 = toFixed(nip, 8)
                biy = int(input("[ 1 ] Apple ("+str(nip2)+"/"+str(MoneyApple2)+") \n[ 2 ] Sumsung ("+str(nip2)+"/"+str(MoneySumsung2)+") \n[ 3 ] Microsoft ("+str(nip2)+"/"+str(MoneyMicrosoft2)+") \n⋗ "))
                break
            except ValueError:
                jojo()
                dog = input("#Error# Oops!  This is the wrong value.  Try again... \n⋗ ")
                jojo()
                mone()
        time.sleep(1)
        if biy == 1:
            if nip >= MoneyApple and Apple == "hor":
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
            if nip >= MoneySumsung and Sumsung == "hor":
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
            if nip >= 0.00000026 and Microsoft == "hor":
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
        nMon2 = toFixed(nMon, 8)
        print(f'Money: ' + str(nMon2))
        time.sleep(1)
        jojo()
        killop()
    elif popi == 4:
        jojo()
        Wallet()
    elif popi == 5:
        jojo()
        bartter()
    #exit from window 2
    elif popi == 6:
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
10 ing()
11 hopy()
12 mone()
13 killop()
14 help
15 exit""")
        Admin()
    elif admin == "exit" or admin == "Exit":
        jojo()
        main()
    else:
        Admin()

if __name__ == "__main__":
    main()