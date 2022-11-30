from api_helper import ShoonyaApiPy
#credentials
import TOTP
# user        = 'FA33870'
# u_pwd       = 'Suseela@26'
# factor2     = TOTP.pin
# vc          = 'FA33870_U'
# app_key     = '2fe120f52ab3d6889b135e38af0a361f'
# imei        = 'abc1234'

user = 'FA71332'
u_pwd = 'SDfighter$44'
factor2 =TOTP.pin
vc = 'FA71332_U'
app_key = 'b9187c771da32847ecfc3902d3b8488c'
imei = 'abc1234'


api = ShoonyaApiPy()
# ret = api.login(userid=user, password=u_pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
# ret = ret['susertoken']
# print("TOKEN TEESUKO RAA REYY : ", ret)
#######################

# f = open('TOKEN','w+')
# f.write(ret)
# f.close()
# print(ret)


k = open("TOKEN",'r')
l = (k.read())
# print(type(k.read()))

# login_status = api.set_session(userid=user, password=u_pwd, usertoken=f.read())
# api = ShoonyaApiPy()
second_login = api.set_session(userid=user,password=u_pwd,usertoken= l )
print(second_login)
# ltp = api.get_quotes(config.exchange, config.instrument)['lp']

# api = ShoonyaApiPy()
LTP = api.get_quotes('NSE','RELIANCE-EQ')['lp']
while True:
    print(LTP)
    exit()
# while True:
#     print(LTP)

