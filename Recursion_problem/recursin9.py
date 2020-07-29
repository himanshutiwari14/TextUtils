def list_of_sum(list1):
    total=0
    for iter in list1:
        if type(iter)==type([]):
            total=total+list_of_sum(iter)
        else:
            total=total+iter
    return total

    


print(list_of_sum([1, 2, [3,4], [5,6]]))