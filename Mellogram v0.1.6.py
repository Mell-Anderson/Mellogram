#[{"name": "Mellogram"}{"version": "0.1.0 beta 5"}{"site": "https://mell-anderson.github.io/Mellogram/index-en.html"}]
try:
    import unlink as un
except ImportError:
    unlink = None
try: 
    import datetime
except ImportError:
    datetime = None
try: 
    import json
except ImportError:
    json = None
#from datetime import date
#today = datetime.datetime.today()
#today2 = today.strftime("%H:%M:%S")
#storage = "/storage/emulated/0/"

bitcoinBuy = 0.00000230
try: 
    import time
except ImportError:
    time = None
try: 
    import tempfile
except ImportError:
    tempfile = None
try: 
    import os
except ImportError: 
    os = None
try: 
    import sys
except ImportError: 
    sys = None
try: 
    import socket
except ImportError: 
    socket = None
try: 
    import threading
except ImportError: 
    threading = None
try:
    from loguru import logger
except ImportError: 
    threading = None

bitcoinSell = 0.00000130

g = True
ark = True

@logger.catch
def pop():
    while True:
        jojo()
        print("Loading ...")
        for i in "▇ ▆ ▅ ▄ ▃ ▂":
            time.sleep(0.3)
            sys.stdout.write(i)
            sys.stdout.flush()
        time.sleep(0.5)
        jojo()
    else: 
        main()

@logger.catch
def is_connected():
    try:
        socket.gethostbyaddr('www.google.com')
        background()
    except socket.gaierror:
        pop()

@logger.catch
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
            
#Standard parameters
nip = float(0.00000000)
bn = 7
n = 5
nMon = 0
kod = " "

#Secondary functions
Apple = "hor"
Sumsung = "hor"
Microsoft = "hor"

@logger.catch
def jojo():
    #Emptiness
    print("\033[H\033[J")

language = "en"
match language:
    case "en":
        pass
    case "ru":
        pass

MoneyApple = 0.00000100
MoneySumsung = 0.00000045
MoneyMicrosoft = 0.00000026

@logger.catch
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
   
CHEAT_CODES = ["God", "Speed"]

@logger.catch
def setting():
    global kod, language, CHEAT_CODES
    kodin = input(f"\nKode: {kod}\nLanguage: {language}\n> ")
    if "/kode " in kodin:
        non0 = kodin.replace("/kode ", "")
        match non0:
            case "God":
                kod = CHEAT_CODES[0]
                ast(4)
                jojo()
                setting()
            case "Speed":
                kod = CHEAT_CODES[1]
                ast(5)
                jojo()
                setting()
    match kodin:
        case "/sekret":
            jojo()
            un.hook("[Mell]", "Have you ever wondered what a question is?")
            dog = input("⋗ ")
            un.hook("[Mell]", "In any case, in my opinion, this is a variable with your or someone else's opinion.")
            dog = input("⋗ ")
            un.hook("[Mell]", "Choose, you decide or for you?")
            dog = input("⋗ ")
            un.hook("[User]", "If you decide that you are not a competitor, then maybe you will leave?")
            dog = input("⋗ ")
            un.hook("[Mell]", "I am waiting...")
            dog = input("⋗ ")
            un.hook("[Mell]", "Well, if you have not left yet, it means that you either have only your own opinion, or you are not tired of my inner voice yet.")
            dog = input("⋗ ")
            un.hook("[Mell]", "So can we get back to reality?")
            dog = input("⋗ ")
            jojo()
            setting()
        case "exit":
            jojo()
            main()
        case _:
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

ANS = ['Yes','Y','yes','y']

@logger.catch
def Shop():
    global Passport2, Machine2, QuantitySell, QuantityBuy, InventoryQuantityMachine, nMon, MachineBuy, PassportBuy, MachineSell, PassportSell, Machine, Passport, InventoryQuantityPassport
    print("I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3")
    print(f"[ 1 ]Machine ({Machine2}/50) \n[Buy: {MachineBuy}$] \n[Sell: {MachineSell}$]\n\n[ 2 ]Passport ({Passport2}/200) \n[Buy: {PassportBuy}$] \n[Sell: {PassportSell}$]\n")
    while True:
        try:
            mnb = input("Select Item: ") #Product selection
            break
        except ValueError:
            jojo()
            Shop()
    if mnb == "3":
            jojo()
            killop()
            while True:
                try:
                    jkp = str(input("Buy or Sell: ")) #Choice of buying and selling
                    break
                except ValueError:
                    jojo()
                    Shop()
    elif mnb == "1" and jkp == "Buy":
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
    elif mnb == "1" and jkp == "Sell":
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
    if mnb ==  "2" and jkp == "Buy":
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
    elif mnb == "2" and jkp == "Sell":
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

@logger.catch
def background():
    if ark:
        un.hook("[Mell]", "Um... how did you get here?")
        dog = input("⋗ ")
        un.hook("[Mell]", "It doesn't matter anymore, go away so I don't have to kill!")
        dog = input("⋗ ")
        un.hook("[Mell]", "Well, if you don't want to leave, I'll help you with that.")
        dog = input("⋗ ")
        un.hook("[User]", "I lost my harvest, I started to fall")
        dog = input("⋗ ")
        main()
    else:
        main()

@logger.catch
def Inventory():
    global InventoryQuantityMachine, InventoryQuantityPassport
    dog = input(f"We have prepared information about your equipment for you, keep. \nMachine: {InventoryQuantityMachine}\n\nPassport: {InventoryQuantityPassport}\n⋗ ")
    killop()

@logger.catch
def main():
    global ark
    logger.debug("That's it, beautiful and simple logging!")
    jojo()
    print("\nHello, well, I think you know me, but that doesn't stop us from talking \n[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Settings \n[ 4 ] - Exit")
    while True:
        try:
            answer = input("⋗ ")
            break
        except ValueError:
            jojo()
            main()
    #Start the game
    match answer:
        case "1":
            jojo()
            killop()
        #Continue game
        case "2":
            jojo()
            main()
        #Settings
        case "3":
            jojo()
            setting()
        #Output
        case "4":
            jojo()
            hopy()
        case _:
            jojo()
            main()

#Window #2

@logger.catch
def killop():
    jojo()
    print("Hello, mountain, today we will mine. \n[ 1 ] Mine - start mining \n[ 2 ] Video card - buying upgrades \n[ 3 ] County - collected money \n[ 4 ] Underground - crypto details \n[ 5 ] Bartter - available temporary work")
    mone()
    

bitcoinBuy2 = toFixed(bitcoinBuy, 8)
bitcoinSell2 = toFixed(bitcoinSell, 8)

@logger.catch
def underground():
    global nMon, nip, bitcoinBuy, bitcoinSell, bitcoinSell2, bitcoinBuy2
    while True:
        try:
            vin = input("Here you can choose the desired currency, exchange or sell it. \n[ 1 ] Exchanger \n[ 2 ] Exchange Rates \n[ 3 ] Buying a ban\n[ 4 ] Inventory \n[ 5 ] exit \n⋗ ")
            break
        except ValueError:
            jojo()
            underground()
    match vin:
        case "1":
            jojo()
            underground()
        case "2":
            jojo()
            bot = input(f"Bitcoin: \nBuy: 100$ = {bitcoinBuy2}\n\nSell: 100$ = {bitcoinSell2}\n\n[Buy or Sell]\n⋗ ")
            match bot:
                case "Buy":
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
                case "Sell":
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
                case _:
                    jojo()
                    dog = input("Please enter buy or sell next time\n⋗ ")
                    jojo()
                    underground()
        case "3":
            jojo()
            Shop()
        case "4":
            jojo()
            Inventory()
        case "5":
            jojo()
            killop()
        case _:
            jojo()
            underground()

@logger.catch
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Process...")
        time.sleep(1)
        num_of_secs -= 1

v3 = "☑"
    
@logger.catch
def video():
    while True:
        try:
            MoneyApple2 = toFixed(MoneyApple, 8)
            MoneySumsung2 = toFixed(MoneySumsung, 8)
            MoneyMicrosoft2 = toFixed(MoneyMicrosoft, 8)
            nip2 = toFixed(nip, 8)
            biy = input(f"Video cards are an important thing in mining, the better the easier it is to mine.\n[ 1 ] GeForce GTX 2080 ({nip2}/{MoneyApple2}) \n[ 2 ] GeForce GTX 1060 ({nip2}/{MoneySumsung2}) \n[ 3 ] GeForce GTX 750 ({nip2}/{MoneyMicrosoft2}) \n⋗ ")
            break
        except ValueError:
            jojo()
            killop()
    match biy:
        case "1":
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
        case "2":
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
        case "3":
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
        case _:
             jojo()
             killop()

@logger.catch
def bartter():
    global nMon, ans, bartter
    while True:
        try:
            contract = input("A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n\n⋗ ")
            break
        except ValueError:
            jojo()
    match contract:
        case "1":
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
            
        case "2":
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
        case "3":
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
        case "exit":
            jojo()
            killop()
        case _:
            jojo()
            bartter()

#Mining
@logger.catch
def mone():
    global nip, MoneySumsung, MoneyApple, MoneyMicrosoft, Apple, Sumsung, Microsoft, nMon, bn, n
    while True:
        try:
            popi = str(input("⋗ "))
            break
        except ValueError:
            jojo()
            killop()
    match popi:
        case "1":
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
                str(un.tim(bn))*pop
                bn = bn/pop
                killop()
            else:
                jojo()
                killop()
                nip2 = toFixed(nip, 8)
                print(f'Bitcoin: {nip2}')
                time.sleep(1)
                jojo()
                killop()
        #Companies
        case "2":
            jojo()
            video()
        #Money
        case "3":
            nip2 = toFixed(nip, 8)
            print(f'Bitcoin: {nip2}')
            time.sleep(1)
            print(f'Money: {nMon}')
            time.sleep(1)
            jojo()
            killop()
        case "4":
            jojo()
            underground()
        case "5":
            jojo()
            bartter()
            #exit from window 2
        case "exit" :
            jojo()
            main()
        case _:
            jojo()
            killop()

#Game Exit Confirmation
@logger.catch
def hopy():
    global ANS
    try:
        bit = input("Exit? \n[ Yes ] [ No ] \n⋗ ")
    except ValueError:
        jojo()
        hopy()
    if bit in ANS:
        quit()
        logger.add("file_{time}.log")
    else:
        jojo()
        main()

if __name__ == "__main__":
    is_connected()