class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.tail=None
class Solution: 
    def display(self,head):
        current = head
        while current:
            print("yha pe luch print hp rha hai")
            print(current.data,end=' ')
            current = current.next
            

  
    def insert(self,head,data):
        if head is None:

            head = Node(data)
            self.tail = head
        else: 
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head

           

print("1")
mylist= Solution()
print("mylist",mylist)
T=int(input())
head=None
for i in range(T):
    print("i index are",i)
    data=int(input())
    print("input data is ",data)
    head=mylist.insert(head,data)
    print("head data is ",head)
mylist.display(head)
	  