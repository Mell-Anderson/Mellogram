import time
import sys
import config as con
try:
    from loguru import logger
except ImportError: 
    threading = None

def jojo():
    #Emptiness
    print("\033[H\033[J")

class Language:
    def __init__(self, language = None):
        self.language = language
        self.message = '0000001'
    
    def PrintLang(self, message_id):
        if self.language is None:
            self.language = "en"
        if self.language == "en":
            if message_id == '0000001':
                return (f'\nKode: {con.kod}\nLanguage: en\n> ')
            elif message_id == '0000002':
                return langEN[message_id]
            elif message_id == '0000003':
                return f"I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3 [1]Machine ({con.Machine2}/50) \n[Buy: {con.MachineBuy}$] \n[Sell: {con.MachineSell}$]\n\n[2]Passport ({con.Passport2}/200) \n[Buy: {con.PassportBuy}$] \n[Sell: {con.PassportSell}$]\n"
            elif message_id == '0000004':
                return langEN[message_id]
        elif self.language == "ru":
            if message_id == '0000001':
                return (f'\nКод: {con.kod}\nЯзык: ru\n> ')
            elif message_id == '0000002':
                return langEN[message_id]
            elif message_id == '0000003':
                return f"За товар объявляю бой, желаю удачи в торге.\nДля выхода нужно написать 3.\n[1]Автоматы ({con.Machine2}/50)[Купить: {con.MachineBuy}$] \n[Продать: {con.MachineSell}$]\n\n[2]Паспорты ({con.Passport2}/200) \n[Купить: {con.PassportBuy}$] \n[Продать: {con.PassportSell}$]"
            elif message_id == '0000004':
                return langRU[message_id]
            elif message_id == '0000005':
                return langRU[message_id]
        else:
            pass

langEN = {'0000002': 'Loading ...', '0000004': 'Select Item: ', '0000005': 'Buy or Sell: '}

langRU = {'0000002': 'Загрузка ...', '0000004': 'Выбрать предмет: ', '0000005': 'Купить или Продать: '}

def tim(job):
    #Animation
    jojo()
    print("0%[••••••••••••••••••••]")
    time.sleep(job)
    jojo()
    print("5%[#•••••••••••••••••••]")
    time.sleep(job)
    jojo()
    print("10%[##•••••••••••••••••]")
    time.sleep(job)
    jojo()
    print("15%[###••••••••••••••••]")
    time.sleep(job)
    jojo()
    print("21%[####•••••••••••••••]")
    time.sleep(job)
    jojo()
    print("26%[#####••••••••••••••]")
    time.sleep(job)
    jojo()
    print("31%[######•••••••••••••]")
    time.sleep(job)
    jojo()
    print("36%[#######••••••••••••]")
    time.sleep(job)
    jojo()
    print("42%[########•••••••••••]")
    time.sleep(job)
    jojo()
    print("47%[#########••••••••••]")
    time.sleep(job)
    jojo()
    print("52%[##########•••••••••]")
    time.sleep(job)
    jojo()
    print("57%[###########••••••••]")
    time.sleep(job)
    jojo()
    print("63%[############•••••••]")
    time.sleep(job)
    jojo()
    print("68%[#############••••••]")
    time.sleep(job)
    jojo()
    print("73%[##############•••••]")
    time.sleep(job)
    jojo()
    print("78%[###############••••]")
    time.sleep(job)
    jojo()
    print("84%[################•••]")
    time.sleep(job)
    jojo()
    print("89%[#################••]")
    time.sleep(job)
    jojo()
    print("94%[##################•]")
    time.sleep(job)
    jojo()
    print("100%[##################]")
    time.sleep(job)
    jojo()
    
def hook(hko, plot, n = None):
    if n is None:
        n = 0.1
    print(hko)
    for i in f"{plot}\n":
        time.sleep(n)
        sys.stdout.write(i)
        sys.stdout.flush()