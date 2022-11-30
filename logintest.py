from api_helper import ShoonyaApiPy
api = ShoonyaApiPy()
user        = 'FA33870'
u_pwd       = 'Suseela@26'
l = '39e13302a079e6f4e6ff56061b605d726f0b77d026aa8e8989eea959280db1ab'
ret = api.set_session(userid=user, password=u_pwd, usertoken=l)
print(ret)