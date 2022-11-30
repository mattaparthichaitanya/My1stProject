import time

from api_helper import ShoonyaApiPy
import credentials
import datetime
import WeddingWaitTime
from pathlib import Path
api = ShoonyaApiPy()
###########################
#########Main Login #############
# ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
# ret = ret['susertoken']
# f = open('TOKEN','w+')
# f.write(ret)
# f.close()
########Token Login###########
k = open("TOKEN",'r')
l = (k.read())
ok = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
token = api.get_quotes('NSE', 'Nifty Bank')['token']
lastBusDay = datetime.datetime.today()
lastBusDay = lastBusDay.replace(hour=WeddingWaitTime.hour, minute=WeddingWaitTime.minutes, second=0, microsecond=0)
ret = api.get_time_price_series(exchange='NSE', token=token, starttime=lastBusDay.timestamp(), interval=5)
bnclose = ret[0]['intc']
print(bnclose)
option_ki_dari_edi = round((int(float(bnclose))), -2)
cehedge_ki_dari_edi = option_ki_dari_edi+1000
pehedge_ki_dari_edi = option_ki_dari_edi-1000
# print(cehedge_ki_dari_edi)
# print(pehedge_ki_dari_edi)
print("BANKNIFTY is at : ",option_ki_dari_edi)
puttoken = f'{"Nifty Bank"} {"PE"} {option_ki_dari_edi}'
calltoken = f'{"Nifty Bank"} {"CE"} {option_ki_dari_edi}'
puthedgetoken = f'{"Nifty Bank"} {"PE"} {pehedge_ki_dari_edi}'
callhedgetoken = f'{"Nifty Bank"} {"PE"} {cehedge_ki_dari_edi}'
put = api.searchscrip(exchange='NFO',searchtext=puttoken)['values'][0]['tsym']
call = api.searchscrip(exchange='NFO',searchtext=calltoken)['values'][0]['tsym']
puthedge = api.searchscrip(exchange='NFO',searchtext=puthedgetoken)['values'][0]['tsym']
callhedge = api.searchscrip(exchange='NFO',searchtext=callhedgetoken)['values'][0]['tsym']
print("ATM PUT :    ",put)
print("ATM CALL :   ",call)
print("CALL HEDGE : ",callhedge)
print("PUT HEDGE :  ",puthedge)
########################################
optionsdatafile = 'Weddingdata'
fileexist = Path(optionsdatafile)
file =open(optionsdatafile,'a+')
file.close()
file = open(optionsdatafile,'r')
fileinformation = file.read()
if 'WEDDING-DEPLOYED' != fileinformation:
    print("WEDDING STRATEGY STARTED")
    while True:
        ######################################################
        #Hedges
        api.place_order(buy_or_sell='B', product_type='M',
                        exchange='NFO', tradingsymbol=callhedge,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' CE BOUGHT')
        api.place_order(buy_or_sell='B', product_type='M',
                        exchange='NFO', tradingsymbol=puthedge,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' PE BOUGHT')
        time.sleep(2)
        ######################################################
        #ATM
        api.place_order(buy_or_sell='S', product_type='M',
                        exchange='NFO', tradingsymbol=call,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' CE SOLD')
        api.place_order(buy_or_sell='S', product_type='M',
                        exchange='NFO', tradingsymbol=put,
                        quantity=0, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks=' PE SOLD')








