import datetime
import time
current_time=datetime.datetime.now()
def sumof_natural(n):
    if n>0:

        if len(str(n))==1:
            time.sleep(1)
            

            return n
        time.sleep(1)
        return sumof_natural(n//10) +n%10
print(sumof_natural(6786))
print(sumof_natural(2350))
print(sumof_natural(4509))
print(sumof_natural(6786))
print(datetime.datetime.now()-current_time)

# print(n)