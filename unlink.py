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
    def __init__(self, language):
        self.language = language
        self.message = '1'
    
    def PrintLang(self, message_id):
        while self.language == "en":
            match message_id:
                case '1':
                    return (f'\nKode: {con.kod}\nLanguage: en\n> ')
                case '3':
                    return f"I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3 \n[1]AK-47 ({con.Machine2}/50) \n[Buy: {con.MachineBuy}$] \n[Sell: {con.MachineSell}$]\n\n[2]Passport ({con.Passport2}/200) \n[Buy: {con.PassportBuy}$] \n[Sell: {con.PassportSell}$]\n"
                case '13':
                    return f'We have prepared information about your equipment for you, keep. \nMachineAK-47: {con.InventoryQuantityMachine}\n\nPassport: {con.InventoryQuantityPassport}\n⋗ '
                case '16':
                    return f'Bitcoin: \nBuy: 100$ = {con.bitcoinBuy2}\n\nSell: 100$ = {con.bitcoinSell2}\n\n[Buy or Sell]\n⋗ ' 
                   case '19':
                       return f'Video cards are an important thing in mining, the better the easier it is to mine.\n[ 1 ] GeForce GTX 2080 ({nip2}/{MoneyApple2}) \n[ 2 ] GeForce GTX 1060 ({nip2}/{MoneySumsung2}) \n[ 3 ] GeForce GTX 750 ({nip2}/{MoneyMicrosoft2}) \n⋗ '
                case '30':
                    return f'Bitcoin: {con.nip2}'
                case '31':
                    return f'Money: {con.nMon}'
                case _:
                    return langEN[message_id]
        while self.language == "ru":
            match message_id:
                case '1':
                    return (f'\nКод: {con.kod}\nЯзык: ru\n> ')
                case '3':
                    return f"За товар объявляю бой, желаю удачи в торге.\nДля выхода нужно написать 3.\n[1]AK-47 ({con.Machine2}/50)[Купить: {con.MachineBuy}$] \n[Продать: {con.MachineSell}$]\n\n[2]Паспорты ({con.Passport2}/200) \n[Купить: {con.PassportBuy}$] \n[Продать: {con.PassportSell}$]"
                case '13':
                    return f'Мы подготовили для вас информацию о вашем оборудовании, сохраняйте. \nAK-47: {con.InventoryQuantityMachine}\n\nПаспортов: {con.InventoryQuantityPassport}\n⋗ '
                case '16':
                    return f'Биткоин: \nКупить: 100$ = {bitcoinBuy2}\n\nПродать: 100$ = {bitcoinSell2}\n\n[Купить или Продать]\n⋗ ' 
                case _:
                    return langRU[message_id]
        else:
            pass

langEN = {
    '4': 'Select Item: ', 
    '5': 'Buy or Sell: ',
    '6': 'Select Quantity: ',
    '7': 'Added a new item to your inventory\n⋗ ',
    '8': 'You do not have enough money or you do not have the necessary material in storage',
    '9': 'You were able to sell the goods, congratulations!\n⋗ ',
    '10': 'You do not have AK-47 in inventory \n⋗ ',
    '11': 'You do not have Passport in inventory \n⋗ ',
    '12': '\n>>> Hello, well, I think you know me, but that doesn\'t stop us from talking \n[ 1 ] - Start a new game \n[ 2 ] - Continue what you started \n[ 3 ] - Settings \n[ 4 ] - Exit',
    '14': '>>> Hello, today we will mine?\n┌───────────────┐      ┌───────────────────┐\n│ [ 1 ] Mine    │      │ [ 2 ] Video card  │\n└───────────────┘      └───────────────────┘\n┌───────────────┐      ┌───────────────────┐\n│ [ 3 ] County  │      │ [ 4 ] Underground │\n└───────────────┘      └───────────────────┘\n┌──────────────────────────────────────────┐\n│··············[ 5 ] Bartter···············│\n└──────────────────────────────────────────┘',
    '15': '>>> Here you can choose the desired currency, exchange or sell it. \n┌─────────────────┐     ┌────────────────────────┐\n│ [ 1 ] Exchanger │     │  [ 2 ] Exchange Rates  │\n└─────────────────┘     └────────────────────────┘\n┌─────────────────┐     ┌────────────────────────┐\n│ [ 4 ] Inventory │     │      [ 3 ] Exit        │\n└─────────────────┘     └────────────────────────┘\n┌────────────────────────────────────────────────┐\n│········[ 5 ] Buying prohibited items···········│\n└────────────────────────────────────────────────┘\n⋗ ',
    '17': 'We did not find the required amount in your account \n⋗ ',
    '18': 'Please enter buy or sell next time\n⋗ '
    '20':'You have successfully purchased a video card\n⋗ '
    '21':'You have less than the required amount.\n⋗ '
    '22':'Working conditions \n\nTime: 1:00h \nMoney: 500$ \n[Yes/No] '
    '23':'How many farms do you want to run?(1/20) \n⋗ '
    '24':'A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n\n⋗ '
    '25':'Countdown finished.'
    '26':'Working conditions \n\nTime: 45m \nMoney: 300$ \n[Yes/No] '
    '27':'\nYou are sure? After all, your device will work for the company \n⋗ '
    '28':'Working conditions \n\nTime: 25m \nMoney: 150$ \n[Yes/No] '
    '29':'The contract has been successfully completed, accept your money \n⋗ '
    '32':'Exit? \n[ Yes ] [ No ] \n⋗ '
    '33':'Um... how did you get here?'
}

langRU = {
    '4': 'Выбрать предмет: ', 
    '5': 'Купить или Продать: ',
    '6': 'Выберите количество: ',
    '7': 'Добавлен новый предмет в ваш инвентарь\n⋗ ',
    '8': 'Вам не хватает денег или у вас нет необходимого материала на складе',
    '9': 'Вы смогли продать товар, поздравляем!\n⋗ ',
    '10': 'У вас нет AK-47 в инвентаре \n⋗ ',
    '11': 'У вас нет паспорта в инвентаре \n⋗ ',
    '12': '\n>>> Здравствуйте, я думаю, вы меня знаете, но это не мешает нам говорить \n[ 1 ] - Начать новую игру \n[ 2 ] - Продолжить то, что вы начали \n[ 3 ] - Настройки \n[ 4 ] - Выход',
    '14':'>>> Здравствуй, сегодня мы будем майнить?\n┌───────────────┐      ┌───────────────────┐\n│ [ 1 ] Майнить │      │ [ 2 ] Видеокарты  │\n└───────────────┘      └───────────────────┘\n┌───────────────┐      ┌───────────────────┐\n│ [ 3 ] Кошелёк │      │  [ 4 ] Подпольe   │\n└───────────────┘      └───────────────────┘\n┌──────────────────────────────────────────┐\n│··············[ 5 ] Бартер················│\n└──────────────────────────────────────────┘',
    '15':'>>> Здесь вы можете выбрать нужную валюту, обменять или продать ее. \n┌─────────────────┐     ┌────────────────────────┐\n│ [ 1 ] Обменник  │     │  [ 2 ] Обменник валют  │\n└─────────────────┘     └────────────────────────┘\n┌─────────────────┐     ┌────────────────────────┐\n│ [ 4 ] Инвентарь │     │     [ 3 ] Выход        │\n└─────────────────┘     └────────────────────────┘\n┌────────────────────────────────────────────────┐\n│·······[ 5 ] Покупка запрещенных вещей··········│\n└────────────────────────────────────────────────┘\n⋗ ',
    '17': 'Мы не нашли нужную сумму на вашем счету \n⋗ ',
    '18': 'Пожалуйста, введите купить или продать в следующий раз\n⋗ '
}

def timer(text):
    tim = 1
    print(text)
    time.sleep(tim)
    print("\033[H\033[J")

def tim(job):
    #Animation
    jojo()
    timer("0%[••••••••••••••••••••]")
    timer("5%[#•••••••••••••••••••]")
    timer("10%[##•••••••••••••••••]")
    timer("15%[###••••••••••••••••]")
    timer("21%[####•••••••••••••••]")
    timer("26%[#####••••••••••••••]")
    timer("31%[######•••••••••••••]")
    timer("36%[#######••••••••••••]")
    timer("42%[########•••••••••••]")
    timer("47%[#########••••••••••]")
    timer("52%[##########•••••••••]")
    timer("57%[###########••••••••]")
    timer("63%[############•••••••]")
    timer("68%[#############••••••]")
    timer("73%[##############•••••]")
    timer("78%[###############••••]")
    timer("84%[################•••]")
    timer("89%[#################••]")
    timer("94%[##################•]")
    timer("100%[##################]")
    
    
def hook(hko, plot, n = None):
    if n is None:
        n = 0.1
    print(hko)
    for i in f"{plot}\n":
        time.sleep(n)
        sys.stdout.write(i)
        sys.stdout.flush()