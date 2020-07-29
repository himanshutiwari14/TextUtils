import sys

class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]

    def pushCharacter(self,s):
        return self.list1.append(s)

    def popCharacter(self):
        return self.list1.pop()

    def enqueueCharacter(self,s):
        return self.list2.append(s)

    def dequeueCharacter(self):
        return self.list2.pop(0)





    # Write your code here

# read the string s