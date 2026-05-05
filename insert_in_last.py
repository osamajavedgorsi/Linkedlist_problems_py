#insert nodes in a Linkedlist.

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

N1= Node(10)
N2= Node(20)
N3= Node(30)

N1.next=N2
N2.next=N3

head= N1
curr= head
print('Original Linked list')
while curr!=None:
    print(curr.data)
    curr=curr.next

#insertion in the end
print('New linkedlist after insertion in the end of the list')
newN3=Node(40)
curr=head
while curr.next!=None:
    # print(curr.data)
    curr=curr.next
curr.next=newN3
curr=head
while curr!=None:
    print(curr.data)
    curr=curr.next