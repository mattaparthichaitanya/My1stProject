from api_helper import ShoonyaApiPy
import credentials
import config
from datetime import datetime
import pandas
import time

api = ShoonyaApiPy()

# ret = api.login(userid=credentials.user, password=credentials.u_pwd, twoFA=credentials.factor2, vendor_code=credentials.vc, api_secret=credentials.app_key, imei=credentials.imei)
# ret = ret['susertoken']
# f = open('TOKEN','w+')
# f.write(ret)
# f.close()
k = open("TOKEN",'r')
l = (k.read())


#ret = api.login(userid=user, password=u_pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

#ret = ret['susertoken']
#f = open('TOKEN','w+')
#f.write(ret)
#f.close()
ret = api.set_session(userid=credentials.user, password=credentials.u_pwd, usertoken=l)
#print(ret)

token = api.get_quotes(config.exchange, config.instrument)['token']
while True:
    if True:
        timenow=str(datetime.now())
        print(timenow)
        timenow1=int(timenow[14:16])-1
        if timenow1==-1:
            timenow1=59
        end = int(datetime(year=(datetime.now()).year, month=(datetime.now()).month, day=(datetime.now()).day, hour=(datetime.now()).hour, minute=(datetime.now()).minute, second=0).timestamp())
        stat = int(datetime(year=(datetime.now()).year, month=(datetime.now()).month, day=(datetime.now()).day, hour=9, minute=15, second=0).timestamp())
        Nifty = api.get_time_price_series(exchange=config.exchange, token=token, starttime=stat, endtime=end, interval=config.candelsize)
        timenow2=int(Nifty[0]['time'][14:16])
        if timenow2!=timenow1:
            print('Candle info updating...')
            continue
        print('**************************************************************************')
        niflen=len(Nifty) - 1

        a = []
        for x in range(niflen, -1, -1):
            # print((Nifty[x]['time']))
            a.append(float(Nifty[x]['intc']))

        print('closing value ',a[niflen])
        stockValues = pandas.DataFrame({'Stock_Values': a})
        ema1 = stockValues.ewm(span=6).mean()
        emalist = ema1['Stock_Values'].tolist()
        candleEMA = round(emalist[niflen], 2)
        print('ema value',candleEMA)

        candlelow = float(Nifty[0]['intl'])
        candlehigh = float(Nifty[0]['inth'])
        candletime = Nifty[0]['time']
        print('candlelowis',candlelow)
        print('candletime is',candletime)

        if float(candlelow) > candleEMA:
            print('Candle found above EMA line')
            emtime = int(datetime(year=(datetime.now()).year, month=(datetime.now()).month, day=(datetime.now()).day, hour=int(candletime[11:13]), minute=int(candletime[14:16]), second=0).timestamp())
            print(datetime.fromtimestamp(emtime+120))
            while True:
                setnoentry=0
                ltp = float(api.get_quotes(config.exchange, config.instrument)['lp'])
                strike = round(int(float(ltp)), -2)
                selection = f'{"Nifty Bank"} {"PE"} {strike}'
                ret = api.searchscrip(exchange='NFO', searchtext=selection)
                symP = ret['values'][0]['tsym']
                if emtime+120 <= int(datetime.now().timestamp()):
                    print('No Entry')
                    setnoentry=1
                    break
                if ltp < candlelow:
                    print('ENTRY BUY TRIGGERED')
                    api.place_order(buy_or_sell='B', product_type='I',
                                    exchange='NFO', tradingsymbol=symP,
                                    quantity=1 * config.lotSize, discloseqty=0, price_type='MKT',
                                    retention='DAY', remarks='ENTRY BUY ORDER')
                    exittrade=0
                    while True:
                        ltp = float(api.get_quotes(config.exchange, config.instrument)['lp'])
                        if ltp <= candlelow-((candlehigh-candlelow)*3):
                            print('Target Hit....%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                            print('EXIT BUY ORDER TRIGGERED-SELL TARGET HIT')
                            api.place_order(buy_or_sell='S', product_type='I',
                                            exchange='NFO', tradingsymbol=symP,
                                            quantity=1 * config.lotSize, discloseqty=0, price_type='MKT',
                                            retention='DAY', remarks='PE TARGET HIT')
                            exittrade=1
                            break
                        if ltp >candlehigh:
                            print('Stoploss Hit..........XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                            print('EXIT BUY ORDER TRIGGERED-SELL SL HIT')
                            api.place_order(buy_or_sell='S', product_type='I',
                                            exchange='NFO', tradingsymbol=symP,
                                            quantity=1 * config.lotSize, discloseqty=0, price_type='MKT',
                                            retention='DAY', remarks='PE SL HIT')
                            exittrade=1
                            break
                        if ((datetime.now()).time()).hour == config.SquareOffHour and (
                                (datetime.now()).time()).minute >= config.SquareOffMin:
                            print('SQUAREDOFF SELL ORDER AT:', ltp)
                            api.place_order(buy_or_sell='S', product_type='I',
                                            exchange='NFO', tradingsymbol=symP,
                                            quantity=1 * config.lotSize, discloseqty=0, price_type='MKT',
                                            retention='DAY', remarks='SQUAREOFF')
                            exit()
                    if exittrade==1:
                        break
            if setnoentry == 1:
                continue
            now1 = datetime.now()
            currentTime = now1.hour * 3600 + now1.minute * 60 + now1.second + now1.microsecond * 0.000001
            targetTime = now1.hour * 3600 + (now1.minute+1) * 60
            waittime = targetTime - currentTime
            if waittime > 0:
                print('Waiting Time ',waittime)
                time.sleep(waittime)
        else:
            print('No candle found above EMA line')
            now1 = datetime.now()
            print (now1.time())
            currentTime = now1.hour * 3600 + now1.minute * 60 + now1.second + now1.microsecond * 0.000001
            targetTime = now1.hour * 3600 + (now1.minute + 1) * 60
            waittime = targetTime - currentTime
            if waittime > 0:
                print('Waiting Time ',waittime)
                time.sleep(waittime)
    print('------------------------------------------------------------------------')
    if ((datetime.now()).time()).hour == config.SquareOffHour and (
        (datetime.now()).time()).minute >= config.SquareOffMin:
        print('Time Aypoyindi')
        break
