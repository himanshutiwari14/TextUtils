def power(a,b):
    if b==1:
        return a
    if b==0:
        return 1
    if a==0:
        return 0
    return power(a,(b-1)) *a

print(power(6,0))