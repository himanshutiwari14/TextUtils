#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def reverse(nums):
    start=0
    end=len(nums)-1
    while start<end:
        var1=nums[start]
        nums[start]=nums[end]
        nums[end]=var1
        start=start+1
        end=end-1
    return nums

print(reverse(["h","e","l","l","o"]))