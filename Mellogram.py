import sys

sys.setswitchinterval(2000)

import os
import time
import os.path

try:
    from loguru import logger
except ImportError:
    os.system('pip install loguru')

logger.add("debug.log",
           format="{time} {level} {message}",
           level="DEBUG",
           rotation="1 MB")

try:
    from alive_progress import alive_bar
except ImportError:
    logger.error("Module live_bar not found")
    os.system('pip install alive-progress')

try:
    import modules.config as con
except ImportError:
    logger.error("Module config not found")
    raise ImportError("Game system file not found: config.py")
con.init()

try:
    from modules.unlink import *
except ImportError:
    logger.error("Module unlink not found")
    raise ImportError("Game system file not found: unlink.py")

loop = Language(con.language)


#Clearing the Dialog Box
@logger.catch
def clear_text() -> None:
    print("\033[H\033[J")


#Resource allocation
@logger.catch
def ast(sos: int) -> None:
    logger.info("Run function ast")
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
    logger.info("End of ast function")


#Game settings
@logger.catch
def setting() -> None:
    """
    The function is used to configure game settings:
    - Cheat codes.
    - Language pack changes.
    """
    global loop
    logger.info("Run function setting")
    try:
        kodin = input(loop.PrintLang('1')).lower()
    except ValueError:
        clear_text()
        setting()
    except KeyboardInterrupt:
        clear_text()
        hopy()
    if "/kode " in kodin:
        non0 = kodin.split(" ")
        if con.__kode_list[0] == non0[1]:
            con.Kod = "God"
            logger.info("Cheat code changed to God")
            ast(4)
            clear_text()
            setting()
        elif con.__kode_list[1] == non0[1]:
            con.Kod = "Speed"
            logger.info("Cheat code changed to Speed")
            ast(5)
            clear_text()
            setting()
    elif "/lang " in kodin:
        non0 = kodin.split(" ")
        if "list" == non0[1]:
            clear_text()
            num = 0
            for i in con.language_list:
                num += 1
                print(f"{num}. {i}")
            _lang = int(input("> "))
            if _lang <= len(con.language_list) and _lang > -1:
                lang_varible = con.language_list[_lang - 1]
                loop = Language(lang_varible)
                logger.info(f"Language changed to {lang_varible}")
            clear_text()
            setting()
    if "/sekret" == kodin:
        logger.info("The secret has been discovered")
        clear_text()
        Local.follower("[Mell]", loop.PrintLang('34'))
        Local.follower("[Mell]", loop.PrintLang('35'))
        Local.follower("[Mell]", loop.PrintLang('36'))
        Local.follower("[User]", loop.PrintLang('37'))
        Local.follower("[Mell]", loop.PrintLang('38'))
        Local.follower("[Mell]", loop.PrintLang('39'))
        Local.follower("[Mell]", loop.PrintLang('40'))
        clear_text()
        setting()
    else:
        clear_text()
        main()
    logger.info("End of setting function")


#Play store
@logger.catch
def shop() -> None:
    """
    The function serves as the sale of in-game items and services.
    """
    logger.info("Run function shop")
    print(loop.PrintLang('3'))
    try:
        ShopMainPrinter = input(loop.PrintLang("4")).lower()
    except ValueError:
        clear_text()
        shop()
    except KeyboardInterrupt:
        hopy()
    if ShopMainPrinter == "3":
        clear_text()
        killop()
        try:
            PurchaseRequest = str(input(loop.PrintLang("5")))
        except ValueError:
            clear_text()
            shop()
        except KeyboardInterrupt:
            hopy()
    elif ShopMainPrinter == "1" and PurchaseRequest == "Buy":
        try:
            con.QuantityBuy = int(input(loop.PrintLang('6'))).lower()
        except ValueError:
            clear_text()
            shop()
        except KeyboardInterrupt:
            hopy()
        if con.Machine > 0 and con.Mon >= con.MachineBuy:
            con.Machine -= int(con.QuantityBuy)
            Machine2 = int(con.Machine)
            con.nMon -= int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine += con.QuantityBuy
            clear_text()
            try:
                input(loop.PrintLang('7'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
        else:
            print(loop.PrintLang('8'))
            try:
                input("⋗ ")
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
    elif ShopMainPrinter == "1" and PurchaseRequest == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('6')).lower()
                break
            except ValueError:
                clear_text()
                shop()
            except KeyboardInterrupt:
                hopy()
        if int(con.InventoryQuantityMachine) >= int(
                con.QuantitySell) and con.QuantityBuy < con.Machine:
            con.Machine += int(con.QuantitySell)
            con.Machine2 = int(con.Machine)
            con.Mon += int(con.MachineBuy) * int(con.QuantityBuy)
            con.InventoryQuantityMachine -= con.QuantityBuy
            clear_text()
            try:
                input(loop.PrintLang('9'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
        else:
            clear_text()
            try:
                print(loop.PrintLang('10'))
                input('\n> ')
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
    if ShopMainPrinter == "2" and PurchaseRequest == "Buy":
        while True:
            try:
                con.QuantityBuy = int(input(loop.PrintLang('06')))
                break
            except ValueError:
                clear_text()
                shop()
            except KeyboardInterrupt:
                hopy()
        if con.Passport > 0 and con.nMon >= con.PassportBuy and con.QuantityBuy < con.Passport:
            con.Passport -= int(con.QuantityBuy)
            con.Passport2 = int(con.Passport)
            con.nMon -= int(con.PassportBuy) * int(con.QuantityBuy)
            con.InventoryQuantityPassport += con.QuantityBuy
            clear_text()
            try:
                print(loop.PrintLang('07'))
                input(f'[{con.UserName}]\n> ')
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
        else:
            clear_text()
            print(loop.PrintLang('08'))
            try:
                input("⋗ ")
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
    elif ShopMainPrinter == "2" and PurchaseRequest == "Sell":
        while True:
            try:
                con.QuantitySell = input(loop.PrintLang('07'))
                break
            except ValueError:
                clear_text()
                shop()
            except KeyboardInterrupt:
                hopy()
        if int(con.InventoryQuantityPassport) >= int(con.QuantitySell):
            con.Passport += int(con.QuantitySell)
            con.Passport2 = int(con.Passport)
            con.nMon += int(con.PassportSell) * int(con.QuantitySell)
            con.InventoryQuantityPassport -= con.QuantitySell
            clear_text()
            try:
                print(loop.PrintLang('09'))
                input('\n> ')
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
        else:
            clear_text()
            try:
                input(loop.PrintLang('11'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            shop()
    else:
        clear_text()
        shop()
    logger.info("End of setting function")

#Game inventory (for game items)
@logger.catch
def Inventory() -> None:
    logger.info("Run function Inventory")
    try:
        input(loop.PrintLang('13'))
    except KeyboardInterrupt:
        hopy()
    underground()
    logger.info("End of inventory function")


#Main initial entry (menu)
@logger.catch
def main() -> None:
    logger.info("Run function main")
    clear_text()
    print(loop.PrintLang('12'))
    while True:
        try:
            answer = input("⋗ ")
            break
        except ValueError:
            clear_text()
            main()
        except KeyboardInterrupt:
            hopy()
    if "1" == answer:
        clear_text()
        killop()
    elif "2" == answer:
        clear_text()
        setting()
    elif "3" == answer:
        clear_text()
        hopy()
    elif "4" == answer:

        def forgot(func):
            return func()

        try:
            x = input("Password: ")
        except KeyboardInterrupt:
            hopy()
        if x == "Mell":
            while True:
                if x == "exit":
                    break
                try:
                    m = input("> ")
                except KeyboardInterrupt:
                    hopy()
                forgot(eval(m))
        else:
            main()
    else:
        clear_text()
        main()
    logger.info("End of main function")


#Function extension
@logger.catch
def killop() -> None:
    logger.info("Run function killop")
    clear_text()
    print(loop.PrintLang('14'))
    mone()


#Underground text function
@logger.catch
def underground() -> None:
    logger.info("Run function underground")
    while True:
        try:
            vin = input(loop.PrintLang('15'))
            break
        except ValueError:
            clear_text()
            underground()
        except KeyboardInterrupt:
            hopy()
    if "1" == vin:
        clear_text()
        underground()
    elif "2" == vin:
        clear_text()
        try:
            bot = input(loop.PrintLang('16')).lower()
        except KeyboardInterrupt:
            hopy()
        if "buy" == bot:
            if con.Mon >= 100:
                con.Mon -= 100
                con.Nip += con.BitcoinBuy
                clear_text()
                underground()
            else:
                clear_text()
                try:
                    input(loop.PrintLang('17'))
                except KeyboardInterrupt:
                    hopy()
                clear_text()
                underground()
        elif "sell" == bot:
            if con.Nip >= con.BitcoinSell:
                con.Nip -= con.BitcoinSell
                con.Mon += int(100)
                clear_text()
                underground()
            else:
                clear_text()
                try:
                    input(loop.PrintLang('17'))
                except KeyboardInterrupt:
                    hopy()
                clear_text()
                underground()
        else:
            clear_text()
            underground()
    elif "3" == vin:
        clear_text()
        shop()
    elif "4" == vin:
        clear_text()
        Inventory()
    elif "5" == vin:
        clear_text()
        killop()
    else:
        clear_text()
        underground()


#Timer
@logger.catch
def countdown(num_of_secs: int) -> None:
    logger.info("Run function countdown")
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print("Process...")
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            hopy()
        num_of_secs -= 1


#Store video adapter
@logger.catch
def video() -> None:
    logger.info("Run function video")
    while True:
        try:
            biy = input(loop.PrintLang('19'))
            break
        except ValueError:
            clear_text()
            killop()
        except KeyboardInterrupt:
            hopy()
    if "1" == biy:
        if con.Nip >= con.MoneyApple and con.Apple == "hor":
            ast(1)
            clear_text()
            Apple = "horo"
            try:
                input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
        else:
            clear_text()
            try:
                input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
    elif "2" == biy:
        if con.Nip >= con.MoneySumsung and con.Sumsung == "hor":
            ast(2)
            clear_text()
            con.Sumsung = "horo"
            try:
                input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
        else:
            clear_text()
            try:
                input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
    elif "3" == biy:
        if con.Nip >= 0.00000026 and con.Microsoft == "hor":
            ast(3)
            clear_text()
            con.Microsoft = "horo"
            try:
                input(loop.PrintLang('20'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
        else:
            clear_text()
            try:
                input(loop.PrintLang('21'))
            except KeyboardInterrupt:
                hopy()
            clear_text()
            video()
    else:
        clear_text()
        killop()


#Barter - exchanging time for money
@logger.catch
def bartter() -> None:
    logger.info("Run function bartter")
    while True:
        try:
            contract = input(loop.PrintLang('24'))
            break
        except ValueError:
            clear_text()
            bartter()
        except KeyboardInterrupt:
            hopy()
    if "1" == contract:
        try:
            barter = input(loop.PrintLang('22'))
        except KeyboardInterrupt:
            hopy()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                hopy()
            if bartterConfirmation in con.ANS:
                print(loop.PrintLang('25'))
                con.Inp = 3600
                countdown(int(con.Inp))
                con.Mon += 500
                try:
                    input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    hopy()
                clear_text()
                bartter()
            else:
                clear_text()
                bartter()
        else:
            clear_text()
            bartter()

    elif "2" == contract:
        try:
            barter = input(loop.PrintLang('26'))
        except KeyboardInterrupt:
            hopy()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                hopy()
            if bartterConfirmation in con.ANS:
                con.Inp = 2700
                countdown(int(con.Inp))
                con.Mon += 300
                try:
                    input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    hopy()
                clear_text()
                bartter()
            else:
                clear_text()
                bartter()
        else:
            clear_text()
            bartter()
    elif "3" == contract:
        try:
            barter = input(loop.PrintLang('28'))
        except KeyboardInterrupt:
            hopy()
        if barter in con.ANS:
            try:
                bartterConfirmation = input(loop.PrintLang('27'))
            except KeyboardInterrupt:
                hopy()
            if bartterConfirmation in con.ANS:
                con.Inp = 1500
                countdown(int(con.Inp))
                con.Mon += 150
                try:
                    input(loop.PrintLang('29'))
                except KeyboardInterrupt:
                    hopy()
                clear_text()
                bartter()
            else:
                clear_text()
                bartter()
        else:
            clear_text()
            bartter()
    else:
        clear_text()
        bartter()
    if "exit" == contract:
        clear_text()
        killop()
    else:
        clear_text()
        bartter()


#Function of the 2nd most important value
@logger.catch
def mone() -> None:
    logger.info("Run function mone")
    while True:
        try:
            popi = str(input("⋗ ")).lower()
            break
        except ValueError:
            clear_text()
            killop()
        except KeyboardInterrupt:
            hopy()
    if "1" == popi:
        clear_text()
        while True:
            try:
                popg = int(input(loop.PrintLang('23')))
                break
            except ValueError:
                clear_text()
                killop()
            except KeyboardInterrupt:
                hopy()
        if popg in range(1, 21):
            con.Mon += (con.MineMoney * popg)
            con.Bn *= popg
            str(tim()) * popg
            con.Bn /= popg
            killop()
        else:
            clear_text()
            killop()
    elif "2" == popi:
        clear_text()
        video()
    elif "3" == popi:
        print(loop.PrintLang('30'))
        time.sleep(1)
        print(loop.PrintLang('31'))
        time.sleep(1)
        clear_text()
        killop()
    elif "4" == popi:
        clear_text()
        underground()
    elif "5" == popi:
        clear_text()
        bartter()
    elif "exit" == popi:
        clear_text()
        main()
    else:
        clear_text()
        killop()


#Trying to organize an exit


@logger.catch
def hopy() -> None:
    logger.info("Run function hopy")
    try:
        try:
            bit = input(loop.PrintLang('32')).lower()
        except KeyboardInterrupt:
            hopy()
    except ValueError:
        clear_text()
        hopy()
    if bit in con.ANS:
        quit()
    else:
        clear_text()
        main()


#Something like a download...
def run(bools=True) -> None:
    logger.info("Run function run")
    if bools is True:
        try:
            with alive_bar(674, ctrl_c=True, title=f'Loading... ') as bar:
                for i in range(692):
                    time.sleep(0.02)
                    bar()
            main()
        except KeyboardInterrupt:
            hopy()
    else:
        main()


if __name__ == "__main__":
    run(con.v3)
