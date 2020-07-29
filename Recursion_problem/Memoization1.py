import time

def calc_square(num):
    print("Computing {}...".format(num))
    time.sleep(1)
    return num*num

result=calc_square(4)
print(result)

result=calc_square(10)
print(result)

result=calc_square(4)
print(result)

result=calc_square(10)
print(result)