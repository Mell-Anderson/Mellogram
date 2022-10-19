import time, sys, os
import config as con

try:
    from loguru import logger
except ImportError:
    os.system('pip install loguru')

#Clearing the Dialog Box
@logger.catch
def clear_text() -> None:
    print("\033[H\033[J")

@logger.catch
def opener(files: str, types: str, text=[]) -> str:
    search = []

    if text == []:
        try:
            with open(files, types) as file:
                readline_text = file.readline()
                search.append(readline_text)
        except FileNotFoundError:
            raise FileNotFoundError(
                f'Directory not found or \'{files}\' not found.')
    else:
        try:
            with open(files, types) as file:
                for text_line in text:
                    file.write(text_line)
                    text.remove(text_line)
        except FileNotFoundError:
            raise FileNotFoundError('Directory not found or file not found.')
    return 'Text added to file.'

#Translation storage class
@logger.catch
class Language(object):

    def __init__(self, language):
        self.language = language
        self.message = '1'

    def PrintLang(self, message_id) -> str:
        if self.language == "ru_RU" or self.language == "ru_UA" or self.language == con.language_list[1]:
            if '1' == message_id:
                return (f'\nКод: {con.Kod}\nЯзык: ru\n> ')
            elif '3' == message_id:
                return f"За товар объявляю бой, желаю удачи в торге.\nДля выхода нужно написать 3.\n[1]AK-47 ({con.Machine2}/50)[Купить: {con.MachineBuy}$] \n[Продать: {con.MachineSell}$]\n\n[2]Паспорты ({con.Passport2}/200) \n[Купить: {con.PassportBuy}$] \n[Продать: {con.PassportSell}$]"
            elif '13' == message_id:
                return f'Мы подготовили для вас информацию о вашем оборудовании, сохраняйте. \nAK-47: {con.InventoryQuantityMachine}\n\nПаспортов: {con.InventoryQuantityPassport}\n⋗ '
            elif '16' == message_id:
                return f'Биткоин: \nКупить: 100$ = {con.BitcoinBuy2}\n\nПродать: 100$ = {con.BitcoinSell2}\n\n[Купить или Продать]\n⋗ '
            elif '30' == message_id:
                return f'Биткоинов: {con.Nip2}'
            elif '31' == message_id:
                return f'Денег: {con.Mon}'
            else:
                return langRU[message_id]
        else:
            if '1' == message_id:
                return (f'\nKode: {con.Kod}\nLanguage: en\n> ')
            elif '3' == message_id:
                return f"I declare a fight for goods, I wish you good luck in a bargain. \nTo exit you need to write 3 \n[1]AK-47 ({con.Machine2}/50) \n[Buy: {con.MachineBuy}$] \n[Sell: {con.MachineSell}$]\n\n[2]Passport ({con.Passport2}/200) \n[Buy: {con.PassportBuy}$] \n[Sell: {con.PassportSell}$]\n"
            elif '13' == message_id:
                return f'We have prepared information about your equipment for you, keep. \nMachineAK-47: {con.InventoryQuantityMachine}\n\nPassport: {con.InventoryQuantityPassport}\n⋗ '
            elif '16' == message_id:
                return f'Bitcoin: \nBuy: 100$ = {con.BitcoinBuy2}\n\nSell: 100$ = {con.BitcoinSell2}\n\n[Buy or Sell]\n⋗ '
            elif '19' == message_id:
                return f'Видеокарты играют важную роль в майнинге, чем лучше, тем проще майнить.\n[ 1 ] GeForce GTX 2080 ({con.Nip2}/{con.MoneyApple2}) \n[ 2 ] GeForce GTX 1060 ({con.Nip2}/{con.MoneySumsung2 }) \n[ 3 ] GeForce GTX 750 ({con.Nip2}/{con.MoneyMicrosoft2}) \n⋗'
            elif '30' == message_id:
                return f'Bitcoin: {con.Nip2}'
            elif '31' == message_id:
                return f'Money: {con.Mon}'
            else:
                return langEN[message_id]


langEN = {
    '4': 'Select Item: ',
    '5': 'Buy or Sell: ',
    '6': 'Select Quantity: ',
    '7': 'Added a new item to your inventory',
    '8':
    'You do not have enough money or you do not have the necessary material in storage',
    '9': 'You were able to sell the goods, congratulations!',
    '10': 'You do not have AK-47 in inventory',
    '11': 'You do not have Passport in inventory',
    '12':
    '\n>>> Hello, well, I think you know me, but that doesn\'t stop us from talking. \n[ 1 ] - Start a new game \n[ 2 ] - Settings \n[ 3 ] - Exit',
    '14':
    '>>> Hello, today we will mine?\n[ 1 ] Mine\n[ 2 ] Video card\n[ 3 ] County\n[ 4 ] Underground\n[ 5 ] Bartter',
    '15':
    '>>> Here you can choose the desired currency, exchange or sell it. \n[ 1 ] Exchanger\n[ 2 ] Exchange Rates\n[ 3 ] Buying prohibited items\n[ 4 ] Inventory\n[ 5 ] Exit\n> ',
    '17': 'We did not find the required amount in your account. ',
    '18': 'Please enter buy or sell next time',
    '20': 'You have successfully purchased a video card',
    '21': 'You have less than the required amount.',
    '22': 'Working conditions \n\nTime: 1:00h \nMoney: 500$ \n[Yes/No] ',
    '23': 'How many farms do you want to run?(1/20)',
    '24':
    'A loan is a responsibility, are you ready to accept it?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n> ',
    '25': 'Countdown finished.',
    '26': 'Working conditions \n\nTime: 45m \nMoney: 300$ \n[Yes/No] ',
    '27': '\nYou are sure? After all, your device will work for the company',
    '28': 'Working conditions \n\nTime: 25m \nMoney: 150$ \n[Yes/No] ',
    '29': 'The contract has been successfully completed, accept your money',
    '32': 'Exit? \n[ Yes ] [ No ]',
    '33': 'Um... how did you get here?',
    '34': 'Have you ever wondered what a question is?',
    '35':
    'In any case, in my opinion, this is a variable with your or someone else\'s opinion.',
    '36': 'Choose, you decide or for you?',
    '37':
    'If you decide that you are not a competitor, then maybe you will leave?',
    '38': 'I am waiting...',
    '39':
    'Well, if you have not left yet, it means that you either have only your own opinion, or you are not tired of my inner voice yet.',
    '40': 'So can we get back to reality?'
}

langRU = {
    '4': 'Выбрать предмет: ',
    '5': 'Купить или Продать: ',
    '6': 'Выберите количество: ',
    '7': 'Добавлен новый предмет в ваш инвентарь',
    '8': 'Вам не хватает денег или у вас нет необходимого материала на складе',
    '9': 'Вы смогли продать товар, поздравляем!',
    '10': 'У вас нет AK-47 в инвентаре',
    '11': 'У вас нет паспорта в инвентаре \n⋗ ',
    '12':
    '\n>>> Здравствуйте, я думаю, вы меня знаете, но это не мешает нам говорить. \n[ 1 ] - Начать новую игру \n[ 2 ] - Настройки \n[ 3 ] - Выход',
    '14':
    '>>> Здравствуй, сегодня мы будем майнить?\n[ 1 ] Майнить\n[ 2 ] Видеокарты \n[ 3 ] Кошелёк\n[ 4 ] Подпольe\n[ 5 ] Бартер',
    '15':
    '>>> Здесь вы можете выбрать нужную валюту, обменять или продать ее. \n[ 1 ] Обменник\n[ 2 ] Обменник валют\n[ 3 ] Покупка запрещенных вещей\n[ 4 ] Инвентарь\n\n[ 5 ] Выход\n⋗ ',
    '17': 'Мы не нашли нужную сумму на вашем счету \n⋗ ',
    '18': 'Пожалуйста, введите купить или продать в следующий раз\n⋗ ',
    '20': 'Вы успешно приобрели видеокарту\n⋗ ',
    '21': 'У вас меньше требуемой суммы.\n⋗ ',
    '22': 'Условия работы\n\nВремя: 1:00 \nДеньги: 500$ \n[Да/Нет] ',
    '23': 'Сколько ферм вы хотите запустить? (1/20) \n⋗ ',
    '24':
    'Кредит — это ответственность, готовы ли вы его принять?\n\n[ 1 ] Apple\n[ 2 ] Sumsung\n[ 3 ] Tesla \n⋗ ',
    '25': 'Обратный отсчет завершен.',
    '26': 'Условия работы\n\nВремя: 45 м \nДеньги: 300$ \n[Да/Нет] ',
    '27': '\nВы уверены? Ведь ваше устройство будет работать на компанию\n⋗ ',
    '28': 'Условия работы\n\nВремя: 25 минут \nДеньги: 150$ \n[Да/Нет] ',
    '29': 'Контракт успешно выполнен, примите деньги\n⋗ ',
    '32': 'Выйти? \n[ Да ] [ Нет ] \n⋗ ',
    '33': 'Эм… как вы сюда попали?',
    '34': 'Вы когда-нибудь задумывались, что такое вопрос?',
    '35':
    'В любом случае, на мой взгляд, это переменная со своим или чужим мнением.',
    '36': 'Выбирать, вам решать или за вас?',
    '37': 'Если вы решите, что вы не конкурент, то, может быть, вы уйдете?',
    '38': 'Я жду...',
    '39':
    'Ну а если ты еще не ушел, значит, у тебя либо только свое мнение, либо ты еще не устал от моего внутреннего голоса.',
    '40': 'Так можем ли мы вернуться в реальность?'
}


#Class for helper functions
@logger.catch
class Local(object):

    def timer(text: str) -> None:
        time.sleep(0.1)
        print(text)
        time.sleep(con.Bn)
        print("\033[H\033[J")

    def reLase(text: str, rePlace: str):
        x = input(text)
        ReText = x
        if rePlace in x:
            ReText = x.replace(rePlace, '')
            return ReText

    def follower(name: str, text: str, TimeWrite: int = None) -> None:
        if TimeWrite is None:
            TimeWrite = 0.1
        print(name)
        for i in f"{text}\n":
            time.sleep(TimeWrite)
            sys.stdout.write(i)
            sys.stdout.flush()
        try:
            dog = input("⋗ ")
        except KeyboardInterrupt:
            exit()

    def check(obj: object, seva=str, *args, **kwargs) -> object:
        #check([1,'2'],list) - True
        return isinstance(obj, seva)


#Animation
@logger.catch
def tim() -> None:
    clear_text()
    Local.timer("0%[••••••••••••••••••••]")
    Local.timer("5%[#•••••••••••••••••••]")
    Local.timer("10%[##•••••••••••••••••]")
    Local.timer("15%[###••••••••••••••••]")
    Local.timer("21%[####•••••••••••••••]")
    Local.timer("26%[#####••••••••••••••]")
    Local.timer("31%[######•••••••••••••]")
    Local.timer("36%[#######••••••••••••]")
    Local.timer("42%[########•••••••••••]")
    Local.timer("47%[#########••••••••••]")
    Local.timer("52%[##########•••••••••]")
    Local.timer("57%[###########••••••••]")
    Local.timer("63%[############•••••••]")
    Local.timer("68%[#############••••••]")
    Local.timer("73%[##############•••••]")
    Local.timer("78%[###############••••]")
    Local.timer("84%[################•••]")
    Local.timer("89%[#################••]")
    Local.timer("94%[##################•]")
    Local.timer("100%[##################]")


if __name__ == '__main__':
    raise SystemError("This file is not the main one.")