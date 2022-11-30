import time
import config
from api_helper import ShoonyaApiPy
from datetime import datetime

api = ShoonyaApiPy()
ret = api.login(userid=config.user, password=config.u_pwd, twoFA=config.factor2, vendor_code=config.vc, api_secret=config.app_key, imei=config.imei)
print(ret)
print ("start")
now = ((datetime.now()).time()).hour
print (now)

while True:
    if ((datetime.now()).time()).hour == config.SquareOffHour and ((datetime.now()).time()).minute >= config.SquareOffMin:
        print('SQUAREDOFF SELL ORDER')
        api.place_order(buy_or_sell='B', product_type='I',
                        exchange=config.exchange, tradingsymbol=config.instrument,
                        quantity=1 * config.lotSize, discloseqty=0, price_type='MKT',
                        retention='DAY', remarks='SQUAREOFF BUY')
        break

    print (datetime.now())

# while True :
#     now = datetime.now()
#     va1 = now.time()
#     if va1.hour == 19 :
#         if va1.minute == 46 :
#             if va1.second > 00 :
#                 print (now)
#                 print ("sucs")
#                 time.sleep.
#                 if va1.second == 59:
#                     break

