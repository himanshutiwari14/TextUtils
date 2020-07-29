def star_pattern(n):
    if n==0:
        print("1")
        return "abc"
    print("2")
    return star_pattern(n-1)* 2

print(star_pattern(5))