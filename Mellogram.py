try:
    from alive_progress.styles import showtime
    from alive_progress import alive_it
    from alive_progress import alive_bar
except ImportError:
    raise ImportError('alive-progress - Not found')
try:
    import unlink as un
except ImportError:
    raise FileError("Game system file not found: unlink.py")
try: 
    import datetime
except ImportError:
    raise ImportError('datetime - Not found')
    
try:
    import config as con
except ImportError:
    raise FileError("Game system file not found: config.py")
con.init() 
try: 
    import time
except ImportError:
    raise ImportError('time - Not found')
try: 
    import tempfile
except ImportError:
    raise ImportError('tempfile - Not found')
try: 
    import os
except ImportError: 
    raise ImportError('os - Not found')
try: 
    import sys
except ImportError: 
    raise ImportError('sys - Not found')
try: 
    import socket
except ImportError: 
    raise ImportError('socket - Not found')
try: 
    import threading
except ImportError: 
    raise ImportError('threading - Not found')
try:
    from loguru import logger
except ImportError:
    raise ImportError('loguru - Not found')
    
loop = un.Language(con.language)

"""
@logger.catch
def pop():
    while True:
        jojo()
        print('loading... ')
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
"""
@logger.catch
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
            

@logger.catch
def jojo():
    #Emptiness
    print("\033[H\033[J")
    #os.system('clear')

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
        if "god" == non0:
            con.kod = "God"
            ast(4)
            jojo()
            setting()
        elif "speed" == non0:
            con.kod = "Speed"
            ast(5)
            jojo()
            setting()
    elif "/lang " in kodin:
        non0 = kodin.replace("/lang ", "")
        if "en" == non0:
            loop = un.Language("en")
        elif "ru" == non0:
            loop = un.Language("ru")
    if "/sekret" == kodin:
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
    elif "exit" == kodin:
        jojo()
        main()
    else:
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
        un.hook("[Mell]", loop.PrintLang('33'))
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
    if "1" == answer:
        jojo()
        killop()
        #Continue game
    elif "2" == answer:
        jojo()
        main()
        #Settings
    elif "3" == answer:
        jojo()
        setting()
        #Output
    elif "4" == answer:
        jojo()
        hopy()
    else:
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
    if "1" == vin:
        jojo()
        underground()
    elif "2" == vin:
        jojo()
        bot = input(loop.PrintLang('16')).lower()
        if "buy" == bot:
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
        elif "sell" == bot:
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
    elif "5" == vin:
        jojo()
        Shop()
    elif "4" == vin:
        jojo()
        Inventory()
    elif "3" == vin:
        jojo()
        killop()
    else:
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
            biy = input(loop.PrintLang('19'))
            break
        except ValueError:
            jojo()
            killop()
    if "1" == biy:
        if con.nip >= con.MoneyApple and con.Apple == "hor":
            ast(1)
            jojo()
            Apple = "horo"
            dog = input(loop.PrintLang('20'))
            jojo()
            video()
        else:
            jojo()
            dog = input(loop.PrintLang('21'))
            jojo()
            video()
    #Samsung
    elif "2" == biy:
        if con.nip >= con.MoneySumsung and con.Sumsung == "hor":
            ast(2)
            jojo()
            con.Sumsung = "horo"
            dog = input(loop.PrintLang('20'))
            jojo()
            video()
        else:
            jojo()
            dog = input(loop.PrintLang('21'))
            jojo()
            video()
    elif "3" == biy:
        if con.nip >= 0.00000026 and con.Microsoft == "hor":
            ast(3)
            jojo()
            con.Microsoft = "horo"
            dog = input(loop.PrintLang('20'))
            jojo()
            video()
        else:
            jojo()
            dog = input(loop.PrintLang('21'))
            jojo()
            video()
    else:
        jojo()
        killop()

@logger.catch
def bartter():
    while True:
        try:
            contract = input(loop.PrintLang('24'))
            break
        except ValueError:
            jojo()
    if "1" == contract:
        bartter = input(loop.PrintLang('22'))
        if bartter in con.ANS:
            bartterConfirmation = input(loop.PrintLang('27'))
            if bartter in con.ANS:
                timeC = 3600
                print(loop.PrintLang('25'))
                con.inp = timeC
                countdown(int(con.inp))
                con.nMon += 500
                dog = input(loop.PrintLang('29'))
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
            
    elif "2" == contract:
        bartter = input(loop.PrintLang('26'))
        if bartter in con.ANS:
            bartterConfirmation = input(loop.PrintLang('27'))
            if bartterConfirmation in con.ANS:
                timeC = 2700
                con.inp = timeC
                countdown(int(con.inp))
                con.nMon += 300
                dog = input(loop.PrintLang('29'))
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
    elif "3" == contract:
        bartter = input(loop.PrintLang('28'))
        if bartter in con.ANS:
            bartterConfirmation = input(loop.PrintLang('27'))
            if bartterConfirmation in con.ANS:
                timeC = 1500
                con.inp = timeC
                countdown(int(con.inp))
                con.nMon += 150
                dog = input(loop.PrintLang('29'))
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
    if "exit" == contract:
        jojo()
        killop()
    else:
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
    if "1" == popi:
        jojo()
        while True:
            try:
                popg = int(input(loop.PrintLang('23')))
                break
            except ValueError:
                jojo()
                killop()
        #Farm
        mineMoney = float(0.00000001)
        if popg in range(21):
            con.nip +=  (mineMoney*popg)
            con.bn = con.bn*popg
            str(un.tim())*popg
            con.bn = con.bn/popg
            killop()
        else:
            con.nip2 = toFixed(con.nip, 8)
            print(loop.PrintLang('30'))
            time.sleep(1)
            jojo()
            killop()
    #Companies
    elif "2" == popi:
        jojo()
        video()
        #Money
    elif "3" == popi:
        print(loop.PrintLang('30'))
        time.sleep(1)
        print(loop.PrintLang('31'))
        time.sleep(1)
        jojo()
        killop()
    elif "4" == popi:
        jojo()
        underground()
    elif "5" == popi:
        jojo()
        bartter()
    elif "exit" == popi:
        jojo()
        main()
    else:
        jojo()
        killop()

#Game Exit Confirmation
@logger.catch
def hopy():
    try:
        bit = input(loop.PrintLang('32')).lower()
    except ValueError:
        jojo()
        hopy()
    if bit in con.ANS:
        quit()
    else:
        jojo()
        main()

def run(bool=True):
    if bool is True:
        with alive_bar(598, ctrl_c=False, title=f'Loading... ') as bar:
            for i in range(598):
                time.sleep(0.02)
                bar()
        main()
    else:
        main()

if __name__ == "__main__":
    run(False)