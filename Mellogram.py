from alive_progress.styles import showtime
from alive_progress import alive_it
from alive_progress import alive_bar
try:
    import unlink as un
except ImportError:
    unlink = None
try: 
    import datetime
except ImportError:
    datetime = None

import config as con
con.init() 
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
    loguru = None
    
loop = un.Language(con.language)

@logger.catch
def pop():
    while True:
        jojo()
        print(loop.PrintLang('02'))
        for i in "▇ ▆ ▅ ▄ ▃ ▂":
            time.sleep(0.3)
            sys.stdout.write(i)
            sys.stdout.flush()
        time.sleep(0.5)
        jojo()
    else: 
        main()
"""
@logger.catch
def is_connected():
    try:
        socket.gethostbyaddr('www.google.com')
        background()
    except socket.gaierror:
        pop()
"""
@logger.catch
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
            

@logger.catch
def jojo():
    #Emptiness
    print("\033[H\033[J")

@logger.catch
def ast(sos):
    #Apple
    if sos == 1:
        con.nip -= con.MoneyApple
        con.bn = 5
        con.n = float(0.00000004)
    elif sos == 2:
        con.nip -= con.MoneySumsung
        con.bn = 3
        con.n = float(0.00000007)
    elif sos == 3:
        con.nip -= con.MoneyMicrosoft
        con.bn = 1
        con.n = float(0.00000012)
    elif sos == 4:
        #God
        con.nip += float(1.00000000)
        con.nMon += 1000
    elif sos == 5:
        #Speed
        con.bn = 0.1
        con.n = float(1.00000000)
   
@logger.catch
def setting():
    global loop
    kodin = input(loop.PrintLang('1')).lower()
    if "/kode " in kodin:
        non0 = kodin.replace("/kode ", "")
        match non0:
            case "god":
                con.kod = "God"
                ast(4)
                jojo()
                setting()
            case "speed":
                con.kod = "Speed"
                ast(5)
                jojo()
                setting()
    elif "/lang " in kodin:
        non0 = kodin.replace("/lang ", "")
        match non0:
            case "en":
                loop = un.Language("en")
            case "ru":
                loop = un.Language("ru")
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

@logger.catch
def Shop():
    print(loop.PrintLang('3'))
    while True:
        try:
            mnb = input(loop.PrintLang("4")).lower() #Product selection
            break
        except ValueError:
            jojo()
            Shop()
    if mnb == "3":
            jojo()
            killop()
            while True:
                try:
                    jkp = str(input(loop.PrintLang("5"))) #Choice of buying and selling
                    break
                except ValueError:
                    jojo()
                    Shop()
    elif mnb == "1" and jkp == "Buy":
        while True:
            try:
                con.QuantityBuy = int(input(loop.PrintLang('6'))).lower()
                break
            except ValueError:
                jojo()
                Shop()
        #Request for the number of things to buy
        if con.Machine > 0 and con.nMon >= con.MachineBuy:
            con.Machine -= int(con.QuantityBuy)
            Machine2 = int(con.Machine)
            con.nMon -= int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine += con.QuantityBuy
            jojo()
            dog = input(loop.PrintLang('7'))
            jojo()
            Shop()
        else:
            print(loop.PrintLang('8'))
            dog = input("⋗ ")
            jojo()
            Shop()
    elif mnb == "1" and jkp == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('6')).lower()
                break
            except ValueError:
                jojo()
                Shop()
        if int(con.InventoryQuantityMachine) >= int(con.QuantitySell) and con.QuantityBuy < con.Machine:
            con.Machine += int(con.QuantitySell)
            con.Machine2 = int(con.Machine)
            con.nMon += int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine -= con.QuantityBuy
            jojo()
            dog = input(loop.PrintLang('9'))
            jojo()
            Shop()
        else:
            jojo()
            dog = input(loop.PrintLang('10'))
            jojo()
            Shop()
    #Passport
    if mnb ==  "2" and jkp == "Buy":
        while True:
            try:
                con.QuantityBuy = int(input(loop.PrintLang('06')))
                break
            except ValueError:
                jojo()
                Shop()
         #Request for the number of things to buy
        if con.Passport > 0 and con.nMon >= con.PassportBuy and con.QuantityBuy < con.Passport:
            con.Passport -= int(con.QuantityBuy)
            con.Passport2 = int(con.Passport)
            con.nMon -= int(con.PassportBuy) * int(con.QuantityBuy)
            con.InventoryQuantityPassport += con.QuantityBuy
            jojo()
            dog = input(loop.PrintLang('07'))
            jojo()
            Shop()
        else:
            jojo()
            print(loop.PrintLang('08'))
            dog = input("⋗ ")
            jojo()
            Shop()
    elif mnb == "2" and jkp == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('07'))
                break
            except ValueError:
                jojo()
                Shop()
        if int(con.InventoryQuantityPassport) >= int(con.QuantitySell):
            con.Passport += int(con.QuantitySell)
            con.Passport2 = int(con.Passport)
            con.nMon += int(con.PassportSell) * int(con.QuantitySell)
            con.InventoryQuantityPassport -= con.QuantitySell
            jojo()
            dog = input(loop.PrintLang('09'))
            jojo()
            Shop()
        else:
            jojo()
            dog = input(loop.PrintLang('11'))
            jojo()
            Shop()
    else:
        jojo()
        Shop()

@logger.catch
def background():
    if con.ark:
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
    dog = input(loop.PrintLang('13'))
    killop()

@logger.catch
def main():
    jojo()
    print(loop.PrintLang('12'))
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
    print(loop.PrintLang('14'))
    mone()

@logger.catch
def underground():
    global bitcoinSell2, bitcoinBuy2
    while True:
        try:
            vin = input(loop.PrintLang('15'))
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
            bot = input(loop.PrintLang('16'))
            match bot:
                case "Buy":
                    if con.nMon >= 100:
                        con.nMon -= 100
                        con.nip += con.bitcoinBuy
                        jojo()
                        underground()
                    else:
                        jojo()
                        dog = input(loop.PrintLang('17'))
                        jojo()
                        underground()
                case "Sell":
                    if con.nip >= con.bitcoinSell:
                        con.nip -= con.bitcoinSell
                        con.nMon += int(100)
                        jojo()
                        underground()
                    else:
                        jojo()
                        dog = input(loop.PrintLang('17'))
                        jojo()
                        underground()
                case _:
                    jojo()
                    dog = input()
                    jojo()
                    underground()
        case "5":
            jojo()
            Shop()
        case "4":
            jojo()
            Inventory()
        case "3":
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
            MoneyApple2 = toFixed(con.MoneyApple, 8)
            MoneySumsung2 = toFixed(con.MoneySumsung, 8)
            MoneyMicrosoft2 = toFixed(con.MoneyMicrosoft, 8)
            nip2 = toFixed(con.nip, 8)
            biy = input(f"Video cards are an important thing in mining, the better the easier it is to mine.\n[ 1 ] GeForce GTX 2080 ({nip2}/{MoneyApple2}) \n[ 2 ] GeForce GTX 1060 ({nip2}/{MoneySumsung2}) \n[ 3 ] GeForce GTX 750 ({nip2}/{MoneyMicrosoft2}) \n⋗ ")
            break
        except ValueError:
            jojo()
            killop()
    match biy:
        case "1":
            if con.nip >= con.MoneyApple and con.Apple == "hor":
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
            if con.nip >= con.MoneySumsung and con.Sumsung == "hor":
                ast(2)
                jojo()
                con.Sumsung = "horo"
                dog = input("You have successfully purchased a video card\n⋗ ")
                jojo()
                video()
            else:
                jojo()
                dog = input("You have less than the required amount.\n⋗ ")
                jojo()
                video()
        case "3":
            if con.nip >= 0.00000026 and con.Microsoft == "hor":
                ast(3)
                jojo()
                con.Microsoft = "horo"
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
    while True:
        try:
            contract = input("A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n\n⋗ ")
            break
        except ValueError:
            jojo()
    match contract:
        case "1":
            bartter = input("Working conditions \n\nTime: 1:00h \nMoney: 500$ \n[Yes/No] ")
            if bartter in con.ANS:
                bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
                if bartter in con.ANS:
                    timeC = 3600
                    print('Countdown finished.')
                    con.inp = timeC
                    countdown(int(con.inp))
                    con.nMon += 500
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
            if bartter in con.ANS:
                bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
                if bartterConfirmation in con.ANS:
                    timeC = 2700
                    con.inp = timeC
                    countdown(int(con.inp))
                    con.nMon += 300
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
            if bartter in con.ANS:
                bartterConfirmation = input("\nYou are sure? After all, your device will work for the company \n⋗ ")
                if bartterConfirmation in con.ANS:
                    timeC = 1500
                    con.inp = timeC
                    countdown(int(con.inp))
                    con.nMon += 150
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
    while True:
        try:
            popi = str(input("⋗ ")).lower()
            break
        except ValueError:
            jojo()
            killop()
    match popi:
        case "1":
            jojo()
            while True:
                try:
                    popg = int(input("How many farms do you want to run?(1/20) \n⋗ ")).lower()
                    break
                except ValueError:
                    jojo()
                    killop()
            #Farm
            mineMoney = float(0.00000001)
            if popg in range(21):
                con.nip +=  (mineMoney*popg)
                con.bn = con.bn*popg
                str(un.tim(con.bn))*popg
                con.bn = con.bn/popg
                killop()
            else:
                jojo()
                killop()
                con.nip2 = toFixed(con.nip, 8)
                print(f'Bitcoin: {con.nip2}')
                time.sleep(1)
                jojo()
                killop()
        #Companies
        case "2":
            jojo()
            video()
        #Money
        case "3":
            print(f'Bitcoin: {con.nip2}')
            time.sleep(1)
            print(f'Money: {con.nMon}')
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
    try:
        bit = input("Exit? \n[ Yes ] [ No ] \n⋗ ").lower()
    except ValueError:
        jojo()
        hopy()
    if bit in con.ANS:
        quit()
    else:
        jojo()
        main()

if __name__ == "__main__":
    with alive_bar(606, ctrl_c=False, title=f'Loading... ') as bar:
        for i in range(606):
            time.sleep(0.02)
            bar()
    main()