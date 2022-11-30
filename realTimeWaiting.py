import time
from datetime import datetime
import config
now = datetime.now()
print (now.time())
currentTime = now.hour *3600 + now.minute * 60 +now.second + now.microsecond * 0.000001
targetTime = config.Lhour*3600 + config.Lmin *60 + 0
waittime = targetTime - currentTime
#print (waittime)
#time.sleep(waittime)
now = datetime.now()
print (now.time())
