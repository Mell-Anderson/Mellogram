import datetime
import os
import time
import sys
import socket
import os.path

try:
    from alive_progress.styles import showtime
    from alive_progress import alive_it
    from alive_progress import alive_bar
except ImportError:
    os.system('pip install alive-progress')

try:
    from loguru import logger
except ImportError:
    os.system('pip install loguru')

try:
    import modules.config as con
except ImportError:
    raise ImportError("Game system file not found: config.py")
con.init() 

try:
    from modules.unlink import *
except ImportError:
    raise ImportError("Game system file not found: unlink.py")


loop = Language(con.language)

#Clearing the Dialog Box
@logger.catch
def jojo() -> None:
    print("\033[H\033[J")

#Resource allocation
@logger.catch
def ast(sos:int) -> None:
    if sos == 1:
        con.Nip -= con.MONEYAPPLE
        con.Bn = 5
        con.MineMoney = 400
    elif sos == 2:
        con.Nip -= con.MONEYSUMSUNG
        con.Bn = 3
        con.MineMoney = 100
    elif sos == 3:
        con.Nip -= con.MONEYMICROSOFT
        con.Bn = 1
        con.MineMoney = 68
    elif sos == 4:
        con.Nip += float(1.00000000)
        con.Mon += 1000
    elif sos == 5:
        con.Bn = 0.1
        con.MineMoney = 10000
   
#Game settings
@logger.catch
def setting() -> None:
    global loop
    try:
        kodin = input(loop.PrintLang('1')).lower()
    except KeyboardInterrupt:
        exit()
    if "/kode " in kodin:
        non0 = kodin.replace("/kode ", "")
        if "god" == non0:
            con.Kod = "God"
            ast(4)
            jojo()
            setting()
        elif "speed" == non0:
            con.Kod = "Speed"
            ast(5)
            jojo()
            setting()
    elif "/lang " in kodin:
        non0 = kodin.replace("/lang ", "")
        if "en" == non0:
            loop = Language("en")
        elif "ru" == non0:
            loop = Language("ru")
    if "/sekret" == kodin:
        jojo()
        Local.follower("[Mell]", loop.PrintLang('34'))
        Local.follower("[Mell]", loop.PrintLang('35'))
        Local.follower("[Mell]", loop.PrintLang('36'))
        Local.follower("[User]", loop.PrintLang('37'))
        Local.follower("[Mell]", loop.PrintLang('38'))
        Local.follower("[Mell]", loop.PrintLang('39'))
        Local.follower("[Mell]", loop.PrintLang('40'))
        jojo()
        setting()
    else:
        jojo()
        main()

#Play store
@logger.catch
def Shop() -> None:
    print(loop.PrintLang('3'))
    try:
        ShopMainPrinter = input(loop.PrintLang("4")).lower()
    except ValueError:
        jojo()
        Shop()
    except KeyboardInterrupt:
        exit()
    if ShopMainPrinter == "3":
            jojo()
            killop()
            try:
                PurchaseRequest = str(input(loop.PrintLang("5")))
            except ValueError:
                jojo()
                Shop()
            except KeyboardInterrupt:
                exit()
    elif ShopMainPrinter == "1" and PurchaseRequest == "Buy":
        try:
            con.QuantityBuy = int(input(loop.PrintLang('6'))).lower()
        except ValueError:
            jojo()
            Shop()
        except KeyboardInterrupt:
            exit()
        if con.Machine > 0 and con.Mon >= con.MachineBuy:
            con.Machine -= int(con.QuantityBuy)
            Machine2 = int(con.Machine)
            con.nMon -= int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine += con.QuantityBuy
            jojo()
            try:
                dog = input(loop.PrintLang('7'))
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
        else:
            print(loop.PrintLang('8'))
            try:
                dog = input("⋗ ")
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
    elif ShopMainPrinter == "1" and PurchaseRequest == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('6')).lower()
                break
            except ValueError:
                jojo()
                Shop()
            except KeyboardInterrupt:
                exit()
        if int(con.InventoryQuantityMachine) >= int(con.QuantitySell) and con.QuantityBuy < con.Machine:
            con.Machine += int(con.QuantitySell)
            con.Machine2 = int(con.Machine)
            con.Mon += int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine -= con.QuantityBuy
            jojo()
            try:
                dog = input(loop.PrintLang('9'))
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
        else:
            jojo()
            try:
                print(loop.PrintLang('10'))
                dog = input('\n> ')
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
    if ShopMainPrinter ==  "2" and PurchaseRequest == "Buy":
        while True:
            try:
                con.QuantityBuy = int(input(loop.PrintLang('06')))
                break
            except ValueError:
                jojo()
                Shop()
            except KeyboardInterrupt:
                exit()
        if con.Passport > 0 and con.nMon >= con.PassportBuy and con.QuantityBuy < con.Passport:
            con.Passport -= int(con.QuantityBuy)
            con.Passport2 = int(con.Passport)
            con.nMon -= int(con.PassportBuy) * int(con.QuantityBuy)
            con.InventoryQuantityPassport += con.QuantityBuy
            jojo()
            try:
                print(loop.PrintLang('07'))
                dog = input(f'[{con.UserName}]\n> ')
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
        else:
            jojo()
            print(loop.PrintLang('08'))
            try:
                dog = input("⋗ ")
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
    elif ShopMainPrinter == "2" and PurchaseRequest == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('07'))
                break
            except ValueError:
                jojo()
                Shop()
            except KeyboardInterrupt:
                exit()
        if int(con.InventoryQuantityPassport) >= int(con.QuantitySell):
            con.Passport += int(con.QuantitySell)
            con.Passport2 = int(con.Passport)
            con.nMon += int(con.PassportSell) * int(con.QuantitySell)
            con.InventoryQuantityPassport -= con.QuantitySell
            jojo()
            try:
                print(loop.PrintLang('09'))
                dog = input('\n> ')
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
        else:
            jojo()
            try:
                dog = input(loop.PrintLang('11'))
            except KeyboardInterrupt:
                exit()
            jojo()
            Shop()
    else:
        jojo()
        Shop()

#Text object
@logger.catch
def background() -> None:
    if con.ark:
        un.follower("[Mell]", loop.PrintLang('33'))
        un.follower("[Mell]", "It doesn't matter anymore, go away so I don't have to kill!")
        un.follower("[Mell]", "Well, if you don't want to leave, I'll help you with that.")
        un.follower("[User]", "I lost my harvest, I started to fall")
        main()
    else:
        main()

#Game inventory (for game items)
@logger.catch
def Inventory() -> None:
    try:
        dog = input(loop.PrintLang('13'))
    except KeyboardInterrupt:
        exit()
    underground()

#Main initial entry (menu)
@logger.catch
def main() -> None:
    jojo()
    print(loop.PrintLang('12'))
    while True:
        try:
            answer = input("⋗ ")
            break
        except ValueError:
            jojo()
            main()
        except KeyboardInterrupt:
            exit()
    if "1" == answer:
        jojo()
        killop()
    elif "2" == answer:
        jojo()
        setting()
    elif "3" == answer:
        jojo()
        hopy()
    elif "4" == answer:
        def forgot(func):     
            return func() 
        try:
            x = input("Password: ")
        except KeyboardInterrupt:
            exit()
        if x == "Mell":
            while True:
                if x == "exit":
                    break
                try:
                    m = input("> ")
                except KeyboardInterrupt:
                    exit()
                forgot(eval(m))
        else:
            main()
    else:
        jojo()
        main()

#Function extension
@logger.catch
def killop() -> None:
    jojo()
    print(loop.PrintLang('14'))
    mone()

#Underground text function
@logger.catch
def underground() -> None:
    while True:
        try:
            vin = input(loop.PrintLang('15'))
            break
        except ValueError:
            jojo()
            underground()
        except KeyboardInterrupt:
            exit()
    if "1" == vin:
        jojo()
        underground()
    elif "2" == vin:
        jojo()
        try:
            bot = input(loop.PrintLang('16')).lower()
        except KeyboardInterrupt:
            exit()
        if "buy" == bot:
            if con.Mon >= 100:
                con.Mon -= 100
                con.Nip += con.BitcoinBuy
                jojo()
                underground()
            else:
                jojo()
                try:
                    dog = input(loop.PrintLang('17'))
                except KeyboardInterrupt:
                    exit()
                jojo()
                underground()
        elif "sell" == bot:
                if con.Nip >= con.BitcoinSell:
                    con.Nip -= con.BitcoinSell
                    con.Mon += int(100)
                    jojo()
                    underground()
                else:
                    jojo()
                    try:
                        dog = input(loop.PrintLang('17'))
                    except KeyboardInterrupt:
                        exit()
                    jojo()
                    underground()
        else:
            jojo()
            underground()
    elif "3" == vin:
        jojo()
        Shop()
    elif "4" == vin:
        jojo()
        Inventory()
    elif "5" == vin:
        jojo()
        killop()
    else:
        jojo()
        underground()

#Timer
@logger.catch
def countdown(num_of_secs:int) -> None:
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Process...")
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit()
        num_of_secs -= 1

#Store video adapter
@logger.catch
def video() -> None:
    while True:
        try:
            biy = input(loop.PrintLang('19'))
            break
        except ValueError:
            jojo()
            killop()
        except KeyboardInterrupt:
            exit()
    if "1" == biy:
        if con.Nip >= con.MoneyApple and con.Apple == "hor":
            ast(1)
            jojo()
            Apple = "horo"
            try:
                dog = input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
        else:
            jojo()
            try:
                dog = input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
    elif "2" == biy:
        if con.Nip >= con.MoneySumsung and con.Sumsung == "hor":
            ast(2)
            jojo()
            con.Sumsung = "horo"
            try:
                dog = input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
        else:
            jojo()
            try:
                dog = input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
    elif "3" == biy:
        if con.Nip >= 0.00000026 and con.Microsoft == "hor":
            ast(3)
            jojo()
            con.Microsoft = "horo"
            try:
                dog = input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
        else:
            jojo()
            try:
                dog = input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                exit()
            jojo()
            video()
    else:
        jojo()
        killop()

#Barter - exchanging time for money
@logger.catch
def bartter() -> None:
    while True:
        try:
            contract = input(loop.PrintLang('24'))
            break
        except ValueError:
            jojo()
            bartter()
        except KeyboardInterrupt:
            exit()
    if "1" == contract:
        try:
            barter = input(loop.PrintLang('22'))
        except KeyboardInterrupt:
            exit()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                exit()
            if bartterConfirmation in con.ANS:
                print(loop.PrintLang('25'))
                con.Inp = 3600
                countdown(int(con.Inp))
                con.Mon += 500
                try:
                    dog = input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    exit()
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
            
    elif "2" == contract:
        try:
            barter = input(loop.PrintLang('26'))
        except KeyboardInterrupt:
            exit()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                exit()
            if bartterConfirmation in con.ANS:
                con.Inp = 2700
                countdown(int(con.Inp))
                con.Mon += 300
                try:
                    dog = input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    exit()
                jojo()
                bartter()
            else:
                jojo()
                bartter()
        else:
            jojo()
            bartter()
    elif "3" == contract:
        try:
            barter = input(loop.PrintLang('28'))
        except KeyboardInterrupt:
            exit()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                exit()
            if bartterConfirmation in con.ANS:
                con.Inp = 1500
                countdown(int(con.Inp))
                con.Mon += 150
                try:
                    dog = input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    exit()
                jojo()
                bartter()
            else:
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

#Function of the 2nd most important value
@logger.catch
def mone() -> None:
    while True:
        try:
            popi = str(input("⋗ ")).lower()
            break
        except ValueError:
            jojo()
            killop()
        except KeyboardInterrupt:
            exit()
    if "1" == popi:
        jojo()
        while True:
            try:
                popg = int(input(loop.PrintLang('23')))
                break
            except ValueError:
                jojo()
                killop()
            except KeyboardInterrupt:
                exit()
        if popg in range(1, 21):
            con.Mon +=  (con.MineMoney*popg)
            con.Bn *= popg
            str(tim())*popg
            con.Bn /= popg
            killop()
        else:
            jojo()
            killop()
    elif "2" == popi:
        jojo()
        video()
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
        
 #Trying to organize an exit

@logger.catch
def hopy() -> None:
    try:
        try:
            bit = input(loop.PrintLang('32')).lower()
        except KeyboardInterrupt:
            exit()
    except ValueError:
        jojo()
        hopy()
    if bit in con.ANS:
        quit()
    else:
        jojo()
        main()

#Something like a download...
def run(bools=True) -> None:
    if bools is True:
        try:
            with alive_bar(674, ctrl_c=True, title=f'Loading... ') as bar:
                for i in range(692):
                    time.sleep(0.02)
                    bar()
            main()
        except KeyboardInterrupt:
            exit()
    else:
        main()

if __name__ == "__main__":
    run(False)
