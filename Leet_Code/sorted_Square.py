class Solution:
    def sortedSquares(self, A):
        start=0
        end=len(A)
        while start<end:
            A[start]=A[start]*A[start]
            start=start+1
            print("1111")
        return sorted(A)

        

s=Solution()
print(s.sortedSquares([-4,-1,0,3,10]))