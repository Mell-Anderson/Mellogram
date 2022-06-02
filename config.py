def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def init():
    global kod, bitcoinSell, g, nip, bn, nMon, kod, Apple, Sumsung, Microsoft, ark, n, language, bitcoinBuy, Apple, Sumsung, Microsoft, MachineBuy, MachineSell, PassportBuy, PassportSell, Machine, Passport, QuantityBuy, QuantitySell, InventoryQuantityMachine, InventoryQuantityPassport, MoneyApple, MoneySumsung, MoneyMicrosoft, ANS, bitcoinSell2, bitcoinBuy2,Passport2, Machine2, nip2
    bitcoinSell = 0.00000130
    bitcoinBuy = 0.00000230
    g = True
    ark = True
    nip = float(0.00000000)
    bn = 7
    n = 5
    nMon = 0
    kod = " "
    Apple = "hor"
    Sumsung = "hor"
    Microsoft = "hor"
    language = "en"
    MachineBuy = 120
    PassportBuy = 87
    MachineSell = 98
    PassportSell = 76
    Machine = 12
    Passport = 34
    QuantityBuy = 0
    QuantitySell = 0
    InventoryQuantityMachine = 0
    InventoryQuantityPassport = 0
    MoneyApple = 0.00000100
    MoneySumsung = 0.00000045
    MoneyMicrosoft = 0.00000026
    ANS = ['Yes','Y','yes','y']
    bitcoinBuy2 = toFixed(bitcoinBuy, 8)
    bitcoinSell2 = toFixed(bitcoinSell, 8)
    Machine2 = toFixed(Machine, 8)
    Passport2 = toFixed(Passport, 8)
    nip2 = toFixed(nip, 8)