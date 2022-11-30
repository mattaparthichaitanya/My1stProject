import pandas
from api_helper import ShoonyaApiPy
from datetime import datetime
import config
from xlwt import Workbook
import TOTP

api = ShoonyaApiPy()
user        = 'FA33870'
u_pwd       = 'Suseela@26'
factor2     = TOTP.pin
vc          = 'FA33870_U'
app_key     = 'b33f428b56ecbc1ee7eaa00409beeff5'
imei        = 'abc1234'


# ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
# print(ret)

k = open("TOKEN",'r')
l = (k.read())

ret = api.set_session(userid=user, password=u_pwd, usertoken=l)
print(ret)

token = (api.get_quotes(config.exchange, config.instrument)['token'])

dayclose = ''
Xmultiplier = 3
candlesize = 1

emafound = overlaptrades = entries = slhit = targethit = pointscaptured = redEMApass = redEMAfail = noentrys =c=d= points =0
issquareoff = candlecolar=date1=''
wb1 = Workbook()

for month in range(11, 12):
    c=d =0

    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Date')
    sheet1.write(0, 1, 'EMA candle size')
    sheet1.write(0, 2, 'Points of Profit or Loss')
    sheet1.write(0, 3, 'Is square off')
    sheet1.write(0, 4, 'Candle color')
    xlsname = ('EMA6ovarlap' + str(month) + '.xls')
    sheet2 = wb1.add_sheet('6EMAbuyOF'+str(month))
    sheet2.write(0, 0, 'Date')
    sheet2.write(0, 1, 'total EMAs count')
    sheet2.write(0, 2, 'ENTRYS')
    sheet2.write(0, 3, 'overlaps')
    sheet2.write(0, 4, 'Points of DAY Profit or Loss')
    sheet2.write(0, 5, 'target HITS')
    sheet2.write(0, 6, 'SL HITS')
    sheet2.write(0, 7, 'noentrys')
    sheet2.write(0, 8, 'redEMAfail')
    sheet2.write(0, 9, 'redEMApass')
    for day in range(25, 26):
        emafound = overlaptrades = entries = slhit = targethit = pointscaptured = redEMApass = redEMAfail = noentrys = points = 0
        issquareoff = candlecolar =date1= ''
        time2 = '27-09-2022 09:00:00'

        if day == 31:
            if month == 4 or month == 6 or month == 9 or month == 11:
                continue
        if month == 2:
            if day == 29 or day == 30 or day == 31:
                continue

        strt = int(datetime(year=2022, month=month, day=day, hour=9, minute=15, second=0).timestamp())
        end = int(datetime(year=2022, month=month, day=day, hour=15, minute=30, second=0).timestamp())
        Nifty = api.get_time_price_series(exchange=config.exchange, token=token, starttime=strt, endtime=end,
                                          interval=candlesize)
        if Nifty == api.get_time_price_series(exchange=config.exchange, token=token, starttime=0):
            print('day error')
            continue

        # print(Nifty)
        # exit()
        a = []
        for x in range(len(Nifty) - 1, -1, -1):
            a.append(float(Nifty[x]['intc']))
            # print(a,x)
        stockValues = pandas.DataFrame({'Stock_Values': a})
        ema1 = stockValues.ewm(span=6).mean()
        emalist = ema1['Stock_Values'].tolist()
        emalist = [round(item, 1) for item in emalist]
        emalist.reverse()
        a.reverse()
        # print(emalist)
        # print(a)
        for x in range(len(Nifty) - 1, -1, -1):
            clow = float(((Nifty)[x]["intl"]))
            chigh = float(((Nifty)[x]["inth"]))
            cclose = float(((Nifty)[x]["intc"]))
            copen = float(((Nifty)[x]["into"]))
            time = (Nifty)[x]["time"]
            # print(clow,cclose,emalist[x],a[x],time)
            # if chigh < emalist[x]:
            #     print('BUY EMA6 candle found at', time)
            #     date1 = time[0:10]
            #     emafound = emafound + 1
            #     candlerange = chigh - clow
            #     target = chigh + (Xmultiplier * candlerange)
            #     if copen>cclose:
            #         candlecolar='red'
            #     if cclose>copen:
            #         candlecolar='green'
            #     hr = int(time[11:13])
            #     min = int(time[14:16])
            #     hr2 = int(time2[11:13])
            #     min2 = int(time2[14:16])
            #     tradelast = (hr2 * 100) + min2
            #     currentlast = (hr * 100) + min + candlesize
            #     # print(tradelast,currentlast)
            #     if tradelast > currentlast:
            #         # print('overlap')
            #         overlaptrades = overlaptrades + 1
            #         continue
            #     if min > 58:
            #         hr = hr + 1
            #         min = 0
            #     trailstart = int(
            #         datetime(year=2022, month=month, day=day, hour=hr, minute=min + 1, second=0).timestamp())
            #     Nifty1 = api.get_time_price_series(exchange=config.exchange, token=token,
            #                                        starttime=trailstart + (60 * candlesize),
            #                                        endtime=trailstart - 60 + (60 * 2 * candlesize), interval=1)
            #     # print(Nifty1)
            #     if Nifty1 == api.get_time_price_series(exchange=config.exchange, token=token, starttime=0):
            #         continue
            #     for y in range(len(Nifty1) - 1, -1, -1):
            #         chigh1 = float(((Nifty1)[y]["inth"]))
            #         clow1 = float(((Nifty1)[y]["intl"]))
            #         time1 = (Nifty1)[y]["time"]
            #         flag = 0
            #         # print(lhigh,llow,time1,y)
            #         if chigh1 > chigh:
            #             issquareoff=''
            #             print('entry found at', time1)
            #             entries = entries + 1
            #             hr1 = int(time1[11:13])
            #             min1 = int(time1[14:16])
            #             if min1 > 58:
            #                 hr1 = hr1 + 1
            #                 min1 = 0
            #             trailstart = int(
            #                 datetime(year=2022, month=month, day=day, hour=hr1, minute=min1 + 1, second=0).timestamp())
            #             Nifty2 = api.get_time_price_series(exchange=config.exchange, token=token,
            #                                                starttime=trailstart + 60, endtime=end,
            #                                                interval=1)
            #             if Nifty2 == api.get_time_price_series(exchange=config.exchange, token=token, starttime=0):
            #                 continue
            #             for z in range(len(Nifty2) - 1, -1, -1):
            #                 chigh2 = float(((Nifty2)[z]["inth"]))
            #                 clow2 = float(((Nifty2)[z]["intl"]))
            #                 time2 = (Nifty2)[z]["time"]
            #
            #                 if z == 0:
            #                     flag = 1
            #                     dayclose = float(((Nifty)[0]["intc"]))
            #                     points = (1 * (clow - dayclose))
            #                     pointscaptured = pointscaptured + points
            #                     print(pointscaptured)
            #                     issquareoff='squaredoff'
            #                     print("points captured", points)
            #                     print()
            #                     break
            #
            #                 if clow2 < clow:
            #                     flag = 1
            #                     print('XXXXXXXXXXXXXXXXX SL hit at', time2, '-', candlerange)
            #                     pointscaptured = pointscaptured - candlerange
            #                     points=-candlerange
            #                     print(pointscaptured)
            #                     slhit = slhit + 1
            #                     if copen > cclose:
            #                         redEMAfail = redEMAfail + 1
            #                         print('redEMAfail')
            #
            #                     break
            #                 if chigh2 > target:
            #                     flag = 1
            #                     print('****************Target Hit mawoo at', time2, candlerange * Xmultiplier)
            #                     targethit = targethit + 1
            #                     pointscaptured = pointscaptured + (candlerange * Xmultiplier)
            #                     print(pointscaptured)
            #                     points=candlerange * Xmultiplier
            #                     if copen > cclose:
            #                         redEMApass = redEMApass + 1
            #                         print('redEMApass')
            #                     break
            #         print('current entries are', entries)
            #         if y == 0 and flag == 0:
            #             print('No Entry Found')
            #             noentrys = noentrys + 1
            #         if flag == 1:
            #             c=c+1
            #             sheet1.write(c, 0, date1)
            #             sheet1.write(c, 1, candlerange)
            #             sheet1.write(c, 2, points)
            #             sheet1.write(c, 3, issquareoff)
            #             sheet1.write(c, 4, candlecolar)
            #             # xlsname = ('EMA6of_' + str(month) + '.xls')
            #             wb.save(xlsname)
            #             break
            if clow > emalist[x]:
                print('SELL EMA6 candle found at', time)
                date1 = time[0:10]
                emafound = emafound + 1
                candlerange = chigh - clow
                target = clow - (Xmultiplier * candlerange)
                if copen>cclose:
                    candlecolar='green'
                if cclose>copen:
                    candlecolar='red'
                hr = int(time[11:13])
                min = int(time[14:16])
                hr2 = int(time2[11:13])
                min2 = int(time2[14:16])
                tradelast = (hr2 * 100) + min2
                currentlast = (hr * 100) + min + candlesize
                # print(tradelast,currentlast)
                if tradelast > currentlast:
                    # print('overlap')
                    overlaptrades = overlaptrades + 1
                    continue
                if min > 58:
                    hr = hr + 1
                    min = 0
                trailstart = int(
                    datetime(year=2022, month=month, day=day, hour=hr, minute=min + 1, second=0).timestamp())
                Nifty1 = api.get_time_price_series(exchange=config.exchange, token=token,
                                                   starttime=trailstart + (60 * candlesize),
                                                   endtime=trailstart - 60 + (60 * 2 * candlesize), interval=1)
                # print(Nifty1)
                if Nifty1 == api.get_time_price_series(exchange=config.exchange, token=token, starttime=0):
                    continue
                for y in range(len(Nifty1) - 1, -1, -1):
                    chigh1 = float(((Nifty1)[y]["inth"]))
                    clow1 = float(((Nifty1)[y]["intl"]))
                    time1 = (Nifty1)[y]["time"]
                    flag = 0
                    # print(lhigh,llow,time1,y)
                    if clow1 < clow:
                        issquareoff=''
                        print('entry found at', time1)
                        entries = entries + 1
                        hr1 = int(time1[11:13])
                        min1 = int(time1[14:16])
                        if min1 > 58:
                            hr1 = hr1 + 1
                            min1 = 0
                        trailstart = int(
                            datetime(year=2022, month=month, day=day, hour=hr1, minute=min1 + 1, second=0).timestamp())
                        Nifty2 = api.get_time_price_series(exchange=config.exchange, token=token,
                                                           starttime=trailstart + 60, endtime=end,
                                                           interval=1)
                        if Nifty2 == api.get_time_price_series(exchange=config.exchange, token=token, starttime=0):
                            continue
                        for z in range(len(Nifty2) - 1, -1, -1):
                            chigh2 = float(((Nifty2)[z]["inth"]))
                            clow2 = float(((Nifty2)[z]["intl"]))
                            copen2 = float(((Nifty2)[z]["into"]))
                            time2 = (Nifty2)[z]["time"]

                            if z == 0:
                                flag = 1
                                dayclose = float(((Nifty)[0]["intc"]))
                                points = (1 * (clow - dayclose))
                                pointscaptured = pointscaptured + points
                                print(pointscaptured)
                                issquareoff='squaredoff'
                                print("points captured", points)
                                print()
                                break

                            if chigh2 > chigh:
                                flag = 1
                                slrange=candlerange
                                if copen2>chigh:
                                    slrange=candlerange+(copen2-chigh)
                                    print('sl in immediate candle')
                                print('XXXXXXXXXXXXXXXXX SL hit at', time2, '-', slrange)
                                pointscaptured = pointscaptured - slrange
                                points=-slrange
                                print(pointscaptured)
                                slhit = slhit + 1
                                if copen > cclose:
                                    redEMAfail = redEMAfail + 1
                                    print('redEMAfail')

                                break
                            if clow2 < target:
                                flag = 1
                                print('****************Target Hit mawoo at', time2, candlerange * Xmultiplier)
                                targethit = targethit + 1
                                pointscaptured = pointscaptured + (candlerange * Xmultiplier)
                                print(pointscaptured)
                                points=candlerange * Xmultiplier
                                if copen > cclose:
                                    redEMApass = redEMApass + 1
                                    print('redEMApass')
                                break
                    print('current entries are', entries)
                    if y == 0 and flag == 0:
                        print('No Entry Found')
                        noentrys = noentrys + 1
                    if flag == 1:
                        c=c+1
                        sheet1.write(c, 0, date1)
                        sheet1.write(c, 1, candlerange)
                        sheet1.write(c, 2, points)
                        sheet1.write(c, 3, issquareoff)
                        sheet1.write(c, 4, candlecolar)
                        xlsname = ('EMA6of_' + str(month) + '.xls')
                        wb.save(xlsname)
                        break
        d=d+1
        sheet2.write(d, 0, date1)
        sheet2.write(d, 1, emafound)
        sheet2.write(d, 2, entries)
        sheet2.write(d, 3, overlaptrades)
        sheet2.write(d, 4, pointscaptured)
        sheet2.write(d, 5, targethit)
        sheet2.write(d, 6, slhit)
        sheet2.write(d, 7, noentrys)
        sheet2.write(d, 8, redEMAfail)
        sheet2.write(d, 9, redEMApass)
        wb1.save('buysell6ema.xls')
        xlsname = ('EMA6f_' + str(month) + '.xls')

print('\nEMA5 Count', emafound, '\nOverlaps', overlaptrades, '\nEntries', entries, '\nStoploss Hits', slhit,
      '\nTarget Hits', targethit, '\nTotal Points Captured', pointscaptured)
print('redEMApass', redEMApass, '\nredEMAfail', redEMAfail, '\nNo Entrys', noentrys)

