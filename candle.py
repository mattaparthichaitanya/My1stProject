import config
from api_helper import ShoonyaApiPy
import realTimeWaiting
import time
from datetime import datetime
import credentials
api = ShoonyaApiPy()
# ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
now = datetime.now()
# api = ShoonyaApiPy()
ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
print(ret)

# ret = ret['susertoken']
# # now = datetime.now()-timedelta(1)
# # filename = now.date()
# # rename = str(filename)
# f = open('TOKEN','w+')
# f.write(ret)
# f.close()
# print(ret)
if realTimeWaiting.waittime > 0:
 print('Waiting till', config.Lhour, ':', config.Lmin, 'to execute')
 time.sleep(realTimeWaiting.waittime)
else:
 print("No wait time")

token = (api.get_quotes (config.exchange,config.instrument)['token'])
strt = datetime(year = now.year, month = now.month, day = now.day, hour=config.Shours, minute=config.Sminutes, second=config.Sseconds).timestamp()
end = datetime(year = now.year, month = now.month, day = now.day, hour=config.Ehours, minute=config.Eminutes, second=config.Eseconds).timestamp()
Nifty = api.get_time_price_series(exchange=config.exchange, token=token,starttime=strt,endtime=end, interval=config.interval)
print(Nifty)

high = float(((Nifty)[0]["inth"]))
bufHigh = high+config.buffer
print(high)

low = float(((Nifty)[0]["intl"]))
bufLow = low - config.buffer
