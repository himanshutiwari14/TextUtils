import datetime
import time

current_time=datetime.datetime.now()
def fab(num):
    if num==0:
        time.sleep(0.5)
        return 0
    if num==1:
        time.sleep(0.5)
        return 1
    time.sleep(0.5)
    return fab(num-1)+fab(num-2)
        
print(fab(7))
print(fab(8))
print(fab(7))
print(datetime.datetime.now()-current_time)