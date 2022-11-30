import math
#import candle
import realTimeWaiting
import time
import config
# from api_helper import ShoonyaApiPy
# from datetime import datetime
# import os
# import credentials
# print ("start")
# api = ShoonyaApiPy()
# ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
# # print(ret)
# #token = api.get_quotes (config.exchange,config.instrument)
# # search = api.searchscrip(config.exchange,config.instrument)
# # ltp = api.get_quotes (config.exchange,config.instrument)
# ltp = api.get_quotes('NSE','INFY-EQ')['lp']
# # inter = int(float(ltp))
# print(ltp)



import credentials
from api_helper import ShoonyaApiPy
print ("start")
api = ShoonyaApiPy()
ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)

# ret = ret['susertoken']
#
# f = open('TOKEN','w+')
# f.write(ret)
# f.close()
# print(ret)
#token = api.get_quotes (config.exchange,config.instrument)
# search = api.searchscrip(config.exchange,config.instrument)
# ltp = api.get_quotes (config.exchange,config.instrument)
ltp = api.get_quotes('NSE','INFY-EQ')['lp']
# inter = int(float(ltp))
print(ltp)
