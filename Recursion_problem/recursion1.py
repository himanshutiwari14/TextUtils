import datetime
import time
current_time=datetime.datetime.now()
print("start time is ",current_time)
def reverse_def(s):
    

    #base case
    if len(s)<=1:
        print("Computing {}...".format(s))
        
        return s
    print("Computing {}...".format(s))
    
    return reverse_def(s[1:]) + s[0]
res=reverse_def("abcd")
print(res)
res=reverse_def("dchg")
print(res)
res=reverse_def("abcd")
print(res)
print("Execution time ",datetime.datetime.now() - current_time)
