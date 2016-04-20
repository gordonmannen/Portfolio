import time
import datetime
from datetime import datetime,timedelta



pdxHQ = datetime.fromtimestamp(time.time())
London = pdxHQ + timedelta(hours=7)
NYCity = pdxHQ + timedelta(hours=3)

# Portland HQ time
(datetime.fromtimestamp(time.time()))
print "Portland Office:  Currently", (pdxHQ.strftime('%A, %m-%d-%Y, %I:%M %p PST'))
print "London Office:  Currently", (London.strftime('%A, %m-%d-%Y, %I:%M %p GMT'))
print "London Office hours of operation:  9AM-9PM daily"
(London)
(London.hour,London.minute)
if London.hour > 8 and London.hour < 21:
    print "London Office is currently OPEN"
else:
    print "London Office is currently CLOSED"

print "New York City Office:  Currently", (NYCity.strftime('%A, %m-%d-%Y, %I:%M %p EST'))
print "New York City Office hours of operation:  9AM-9PM daily"
(NYCity)
(NYCity.hour,NYCity.minute)
if NYCity.hour > 8 and NYCity.hour < 21:
    print "New York City Office is currently OPEN"
else:
    print "New York City Office is currently CLOSED"



