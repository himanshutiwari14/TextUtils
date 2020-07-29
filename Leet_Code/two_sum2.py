def new_pr(nums):
    target=9
    nums=list(enumerate(nums))
    start=0
    end=len(nums)-1
    while start<end:        
        if nums[start][1]+nums[end][1]>target:
            end=end-1
        elif nums[start][1]+nums[end][1]<target:
            start=start+1
        elif nums[start][1]+nums[end][1]==target:
    return nums[start][0]+1,nums[end][0]+1
        
print(new_pr([2,7,11,15]))