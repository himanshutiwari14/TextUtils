def sum_two(n):
    #base case
    if n==0:
        return 0
    return sum_two(n-2)+n
print(sum_two(6))