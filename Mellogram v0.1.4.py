#[{name: Mellogram}{version: 0.1.0 beta 4}{site: "https://mell-anderson.github.io/Mellogram/index-en.html"}]
import time
import tempfile
import os
import sys

#Standard password
passwordAdmin = "Admin"

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

ark = False
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

ans = ['Yes','Y','yes','y']

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

language = "en"

if language == "en":
    pass
elif language == "ru":
    pass

MoneyApple = 0.00000100
MoneySumsung = 0.00000045
MoneyMicrosoft = 0.00000026

def ast(sos):
    global nip, bn, n, nMon, MoneyApple, MoneySumsung, MoneyMicrosoft
    #Apple
    if sos == 1:
        nip -= MoneyApple
        bn = 5
        n = float(0.00000004)
    elif sos == 2:
        nip -= MoneySumsung
        bn = 3
        n = float(0.00000007)
    elif sos == 3:
        nip -= MoneyMicrosoft
        bn = 1
        n = float(0.00000012)
    elif sos == 4:
        #God
        nip += float(1.00000000)
        nMon += 1000
    elif sos == 5:
        #Speed
        bn = 0.1
        n = float(1.00000000)
   
def setting():
    global kod, storage, language
    kodin = input(f"Here you will find what you need, I propose to change the rules. \nKode: {kod}\nStorage: ..{storage}\nLanguage: {language}\n⋗ ")
    if kodin == "God":
        kod = "God"
        ast(4)
        jojo()
        setting()
    elif kodin == "Speed":
        kod = "Speed"
        ast(5)
        jojo()
        setting()
    elif kodin == "Storage" or kodin == "storage":
        jojo()
        loop = input("Write a directory where game data can be stored \n⋗ ")
        isDirectory = os.path.isdir(loop)
        if isDirectory == False:
            dog = input("This path does not exist \n⋗ ")
            jojo()
            setting()
        else:
            jojo()
            dog = input("Great, your directory has been saved. \n⋗ ")
            storage = loop
            jojo()
            setting()
    elif kodin == "sekret":
        jojo()
        print("[Mell] ")
        for i in "Have you ever wondered what a question is?":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "In any case, in my opinion, this is a variable with your or someone else's opinion.":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "Choose, you decide or for you?":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "If you decide that you are not a competitor, then maybe you will leave?": 
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "I am waiting...": 
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "Well, if you have not left yet, it means that you either have only your own opinion, or you are not tired of my inner voice yet.": 
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "So can we get back to reality?":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        jojo()
        setting()
    elif kodin == "exit":
        jojo()
        main()
    else:
        jojo()
        setting()

#Price per unit
MachineBuy = 120
PassportBuy = 87
MachineSell = 98
PassportSell = 76
#Quantity
Machine = 12
Passport = 34
Machine2 = Machine
Passport2 = Passport

QuantityBuy = 0
QuantitySell = 0

InventoryQuantityMachine = 0
InventoryQuantityPassport = 0

def Shop():
    global Passport2, Machine2, QuantitySell, QuantityBuy, InventoryQuantityMachine, nMon, MachineBuy, PassportBuy, MachineSell, PassportSell, Machine, Passport, InventoryQuantityPassport
    print("I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3")
    print(f"[ 1 ]Machine ({Machine2}/50) \n[Buy: {MachineBuy}$] \n[Sell: {MachineSell}$]\n\n[ 2 ]Passport ({Passport2}/200) \n[Buy: {PassportBuy}$] \n[Sell: {PassportSell}$]\n")
    while True:
        try:
            mnb = int(input("Select Item: ")) #Product selection
            break
        except ValueError:
            jojo()
            Shop()
    if mnb == 3:
        jojo()
        killop()
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
        if Machine > 0 and nMon >= MachineBuy:
            Machine -= int(QuantityBuy)
            Machine2 = int(Machine)
            nMon -= int(MachineBuy) * int(QuantityBuy)
            InventoryQuantityMachine += QuantityBuy
            jojo()
            dog = input("Added a new item to your inventory\n⋗ ")
            jojo()
            Shop()
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
        if int(InventoryQuantityMachine) >= int(QuantitySell) and QuantityBuy < Machine:
            Machine += int(QuantitySell)
            Machine2 = int(Machine)
            nMon += int(MachineBuy) * int(QuantityBuy)
            InventoryQuantityMachine -= QuantityBuy
            jojo()
            dog = input("You were able to sell the goods, congratulations!\n⋗ ")
            jojo()
            Shop()
        else:
            jojo()
            dog = input("You do not have Machine in inventory \n⋗ ")
            jojo()
            Shop()
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
        if Passport > 0 and nMon >= PassportBuy and QuantityBuy < Passport:
            Passport -= int(QuantityBuy)
            Passport2 = int(Passport)
            nMon -= int(PassportBuy) * int(QuantityBuy)
            InventoryQuantityPassport += QuantityBuy
            jojo()
            dog = input("Added a new item to your inventory\n⋗ ")
            jojo()
            Shop()
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
        if int(InventoryQuantityPassport) >= int(QuantitySell):
            Passport += int(QuantitySell)
            Passport2 = int(Passport)
            nMon += int(PassportSell) * int(QuantitySell)
            InventoryQuantityPassport -= QuantitySell
            jojo()
            dog = input("You were able to sell the goods, congratulations!")
            jojo()
            Shop()
        else:
            jojo()
            dog = input("You do not have Passport in inventory \n⋗ ")
            jojo()
            Shop()
    else:
        jojo()
        Shop()

def Inventory():
    global InventoryQuantityMachine, InventoryQuantityPassport
    dog = input(f"We have prepared information about your equipment for you, keep. \nMachine: {InventoryQuantityMachine}\n\nPassport: {InventoryQuantityPassport}\n⋗ ")
    killop()

def background():
    if ark == True:
        print("[Mell] ")
        for i in "Um... how did you get here?":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "It doesn't matter anymore, go away so I don't have to kill!":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[Mell] ")
        for i in "Well, if you don't want to leave, I'll help you with that.":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        print("[User] ")
        for i in "I lost my harvest, I started to fall":
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        dog = input("\n⋗ ")
        main()
    else:
        main()

def main():
    global ark
    jojo()
    print("\nHello, well, I think you know me, but that doesn't stop us from talking \n[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Settings \n[ 4 ] - Exit")
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
    #Settings
    elif answer == 3:
        jojo()
        setting()
    #Output
    elif answer == 4:
        jojo()
        hopy()
    else:
        jojo()
        main()

#Window #2
def killop():
    jojo()
    print("Hello, mountain, today we will mine. \n[ 1 ] Mine - start mining \n[ 2 ] Video card - buying upgrades \n[ 3 ] County - collected money \n[ 4 ] Underground - crypto details \n[ 5 ] Bartter - available temporary work \n[ 6 ] exit - go back ")
    mone()
    
bitcoinBuy = 0.00000236
bitcoinSell = 0.00000138
bitcoinBuy2 = toFixed(bitcoinBuy, 8)
bitcoinSell2 = toFixed(bitcoinSell, 8)

def underground():
    global nMon, nip, bitcoinBuy, bitcoinSell, bitcoinSell2, bitcoinBuy2
    while True:
        try:
            vin = int(input("Here you can choose the desired currency, exchange or sell it. \n[ 1 ] Exchanger \n[ 2 ] Exchange Rates \n[ 3 ] Buying a ban\n[ 4 ] Inventory \n[ 5 ] exit \n⋗ "))
            break
        except ValueError:
            jojo()
            underground()
    if vin == 1:
        jojo()
        underground()
    elif vin == 2:
        jojo()
        bot = input(f"Bitcoin: \nBuy: 100$ = {bitcoinBuy2}\n\nSell: 100$ = {bitcoinSell2}\n\n[Buy or Sell]\n⋗ ")
        if bot == "Buy":
            if nMon >= 100:
                nMon -= 100
                nip += bitcoinBuy
                jojo()
                underground()
            else:
                jojo()
                dog = input("We did not find the required amount in your account \n⋗ ")
                jojo()
                underground()
        elif bot == "Sell":
            if nip >= bitcoinSell:
                nip -= bitcoinSell
                nMon += int(100)
                jojo()
                underground()
            else:
                jojo()
                dog = input("We did not find the required amount in your account \n⋗ ")
                jojo()
                underground()
        else:
            jojo()
            dog = input("Please enter buy or sell next time\n⋗ ")
            jojo()
            underground()
    elif vin == 3:
        jojo()
        Shop()
    elif vin == 4:
        jojo()
        Inventory()
    elif vin == 5:
        jojo()
        killop()
    else:
        jojo()
        underground()

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Process...")
        time.sleep(1)
        num_of_secs -= 1

def video():
    while True:
        try:
            MoneyApple2 = toFixed(MoneyApple, 8)
            MoneySumsung2 = toFixed(MoneySumsung, 8)
            MoneyMicrosoft2 = toFixed(MoneyMicrosoft, 8)
            nip2 = toFixed(nip, 8)
            biy = int(input(f"Video cards are an important thing in mining, the better the easier it is to mine.\n[ 1 ] GeForce GTX 2080 ({nip2}/{MoneyApple2}) \n[ 2 ] GeForce GTX 1060 ({nip2}/{MoneySumsung2}) \n[ 3 ] GeForce GTX 750 ({nip2}/{MoneyMicrosoft2}) \n⋗ "))
            break
        except ValueError:
            jojo()
            killop()
    if biy == 1:
        if nip >= MoneyApple and Apple == "hor":
            ast(1)
            jojo()
            Apple = "horo"
            dog = input("You have successfully purchased a video card\n⋗ ")
            jojo()
            video()
        else:
            jojo()
            dog = input("You have less than the required amount.\n⋗ ")
            jojo()
            video()
    #Samsung
    elif biy == 2:
        if nip >= MoneySumsung and Sumsung == "hor":
            ast(2)
            jojo()
            Sumsung = "horo"
            dog = input("You have successfully purchased a video card\n⋗ ")
            jojo()
            video()
        else:
            jojo()
            dog = input("You have less than the required amount.\n⋗ ")
            jojo()
            video()
    elif biy == 3:
        if nip >= 0.00000026 and Microsoft == "hor":
            ast(3)
            jojo()
            Microsoft = "horo"
            dog = input("You have successfully purchased a video card\n⋗ ")
            jojo()
            video()
        else:
            jojo()
            dog = input("You have less than the required amount.\n⋗ ")
            jojo()
            video()
    else:
         jojo()
         killop()

def bartter():
    global nMon, ans, bartter
    while True:
        try:
            contract = input("A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n\n⋗ ")
            break
        except ValueError:
            jojo()
    if contract == "1":
        bartter = input("Working conditions \n\nTime: 1:00h \nMoney: 500$ \n[Yes/No] ")
        if bartter in ans:
            bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
            if bartter in ans:
                timeC = 3600
                print('Countdown finished.')
                inp = timeC
                countdown(int(inp))
                nMon += 500
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
            
    elif contract == "2":
        bartter = input("Working conditions \n\nTime: 45m \nMoney: 300$ \n[Yes/No] ")
        if bartter in ans:
            bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
            if bartterConfirmation == "Yes" or bartterConfirmation == "yes" or bartterConfirmation == "y" or bartterConfirmation == "Y":
                timeC = 2700
                inp = timeC
                countdown(int(inp))
                nMon += 300
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
    elif contract == "3":
        bartter = input("Working conditions \n\nTime: 25m \nMoney: 150$ \n[Yes/No] ")
        if bartter in ans:
            bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
            if bartterConfirmation in ans:
                timeC = 1500
                inp = timeC
                countdown(int(inp))
                nMon += 150
                dog = input("The contract has been successfully completed, accept your money \n⋗ ")
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
    elif contract =="exit":
        jojo()
        killop()
    else:
        jojo()
        bartter()

#Mining
def mone():
    global nip, MoneySumsung, MoneyApple, MoneyMicrosoft, Apple, Sumsung, Microsoft, nMon, bn, n
    while True:
        try:
            popi = int(input("⋗ "))
            break
        except ValueError:
            jojo()
            killop()
    if popi == 1:
        jojo()
        while True:
            try:
                pop = int(input("How many farms do you want to run?(1/20) \n⋗ "))
                break
            except ValueError:
                jojo()
                killop()
        #Farm
        mineMoney = float(0.00000001)
        if pop in range(1, 21):
            nip += mineMoney*pop
            bn = bn*pop
            str(tim())*pop
            bn = bn/pop
        else:
            jojo()
            killop()
        nip2 = toFixed(nip, 8)
        print(f'Bitcoin: {nip2}')
        time.sleep(1)
        jojo()
        killop()
    #Companies
    elif popi == 2:
        jojo()
        video()
    #Money
    elif popi == 3:
        nip2 = toFixed(nip, 8)
        print(f'Bitcoin: {nip2}')
        time.sleep(1)
        print(f'Money: {nMon}')
        time.sleep(1)
        jojo()
        killop()
    elif popi == 4:
        jojo()
        underground()
    elif popi == 5:
        jojo()
        bartter()
    #exit from window 2
    elif popi == 6:
        jojo()
        main()
    else:
        jojo()
        killop()

#Game Exit Confirmation
def hopy():
    global ans
    while True:
        try:
            bit = str(input("Exit? \n[ Yes ] [ No ] \n⋗ "))
            break
        except ValueError:
            jojo()
            hopy()
    if bit in ans:
        exit()
    else:
        jojo()
        main()

if __name__ == "__main__":
    background()