import locale
import ctypes


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def init():
    global __kode_list, language_list, Kod, v3, BitcoinSell, Nip, Bn, Mon, Apple, Sumsung, Microsoft, Ark, language, BitcoinBuy, Apple, Sumsung, Microsoft, MachineBuy, MachineSell, PassportBuy, PassportSell, Machine, Passport, QuantityBuy, QuantitySell, InventoryQuantityMachine, InventoryQuantityPassport, MoneyApple, MoneySumsung, MoneyMicrosoft, ANS, BitcoinSell2, BitcoinBuy2,Passport2, Machine2, Nip2, MoneyApple2, MoneySumsung2, MoneyMicrosoft2, MineMoney
    language_list = ['en', 'ru']
    __kode_list = ['god', 'speed']
    windll = ctypes.windll.kernel32
    BitcoinSell = 0.00000130
    BitcoinBuy = 0.00000230
    Ark = True
    Nip = float(0.00000000)
    Bn = 7
    Mon = 0
    Kod = " "
    Apple = "hor"
    Sumsung = "hor"
    Microsoft = "hor"
    language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
    MachineBuy = 120
    PassportBuy = 87
    MachineSell = 98
    PassportSell = 76
    MineMoney = 1
    Machine = 12
    Passport = 34
    QuantityBuy = 0
    QuantitySell = 0
    ANS = ['Yes','Y','yes','y', 'Да','Д','да','д']
    InventoryQuantityMachine = 0
    InventoryQuantityPassport = 0
    MONEYAPPLE = 0.00000100
    MONEYSUMSUNG = 0.00000045
    MONEYMICROSOFT = 0.00000026
    MoneyApple2 = toFixed(MONEYAPPLE, 8)
    MoneySumsung2 = toFixed(MONEYSUMSUNG, 8)
    MoneyMicrosoft2 = toFixed(MONEYMICROSOFT, 8)
    BitcoinBuy2 = toFixed(BitcoinBuy, 8)
    BitcoinSell2 = toFixed(BitcoinSell, 8)
    Machine2 = toFixed(Machine, 8)
    Passport2 = toFixed(Passport, 8)
    Nip2 = toFixed(Nip, 8)
    v3 = False

if __name__ == '__main__':
    raise SystemError("This file is not the main one.")