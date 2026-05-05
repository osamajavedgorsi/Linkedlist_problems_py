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

#inserting node in the beginning
newN1= Node(5)
newN1.next=head
head=newN1
curr=head
print('New linkedlist after insertion in the beginning of the list')
while curr!=None:
    print(curr.data)
    curr=curr.next


#insertion in the kth position
newN2= Node(15)
curr=head
k=2
print('New linkedlist after insertion in middle of the list')
for i in range(k-1):
    # print(curr.data)
    curr=curr.next
newN2.next=curr.next
curr.next=newN2
curr=head
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