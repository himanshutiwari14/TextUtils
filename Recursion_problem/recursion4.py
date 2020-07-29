def fib_series(n):
    if n==1:
        return n
    elif n==0:
        return 0
    
    return fib_series(n-1)+fib_series(n-2)

print(fib_series(12))