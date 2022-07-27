import pickle
from modules.config import *

NameFile = None

def load(NameFile, Password):
    with open(f'LOG/{NameFile}.pkl') as f:
        NameFile, Password, BitcoinSell, BitcoinBuy, Ark, Nip, Bn, Mon, Kod, Apple, Sumsung, Microsoft, language, MachineBuy, PassportBuy, MachineSell, MineMoney, Machine, Passport, QuantityBuy, QuantitySell, ANS, InventoryQuantityMachine, InventoryQuantityPassport, MoneyApple, MoneySumsung, MoneyMicrosoft, MoneyApple2, MoneySumsung2, MoneyMicrosoft2, BitcoinBuy2, BitcoinSell2, Machine2, Passport2, Nip2, v3 = pickle.load(f)