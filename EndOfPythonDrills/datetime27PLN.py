import datetime
import time


pdx_local = datetime.datetime.now()
pdx_local_hour = pdx_local.hour
print (pdx_local.strftime("The local time in Portland is %I:%M%p"))

nyc_local = datetime.datetime.now() + datetime.timedelta(hours = 3)
nyc_local_hour = nyc_local.hour
print (nyc_local.strftime("The local time in NYC is %I:%M%p"))


lon_local = datetime.datetime.now() + datetime.timedelta(hours = 8)
lon_local_hour = lon_local.hour
print (lon_local.strftime("The local time in London is %I:%M%p"))

#d1=datetime.time(9,0)
#print d1.strftime("%H:%M")
#d2=datetime.time(21,0)
#print d2.strftime("%H:%M")


if pdx_local_hour >= 9 and pdx_local_hour <= 21:
    print ("Pdx office is open")
else:
    print ("Pdx office is closed")


if nyc_local_hour >=9 and nyc_local_hour <= 21:
    print ("Nyc office is open")
else:
    print ("Nyc office is closed")


if lon_local_hour >=9 and lon_local_hour <= 21:
    print ("Lon office is open")
else:
    print ("Lon office is closed")



           
