def fact(n):
    print("bhai pehla base case",n)
    #base case
    if n==0:
        print("yha mat aao",n)

        return 1
    print("ye aap ki baap ki jagah hau",n)
    # print(n,"1")
    # print(fact(n-1),"2")
    # print(n*fact(n-1),"3")
    return n*fact(n-1)
print(fact(6))
