from api_helper import ShoonyaApiPy
api = ShoonyaApiPy()
import credentials
import pandas as pd
import config



#print(ret)
print("::::::::::::LOGIN AYYA MOWAAA::::::::::::::::::::::::")

ltp = api.get_quotes('NSE','Nifty Bank')['lp']
print("ORIGINAL LTP :",ltp)
strike = round(int(float(ltp)),-2)
print("STRIKE PRICE :",strike)

#selecting CE option when High of inside bar breach in INDEX of Banknifty
# selection = f'{config.instrument} {config.opce} {strike} '
# print(selection)
# optionexchange = 'NFO'
# ret = api.searchscrip(exchange=optionexchange, searchtext=selection)
# print(ret)
# symC = ret['values'][0]['tsym']
# print (symC)

#selecting PE option when High of inside bar breach in INDEX of Banknifty
selection = f'{"Nifty Bank"} {"PE"} {strike} '
optionexchange = 'NFO'
ret = api.searchscrip(exchange='NFO', searchtext=selection)
symP = ret['values'][0]['tsym']
# print (symP)
