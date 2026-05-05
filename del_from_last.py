                              #Deleting node from last

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

Na= Node(5)
Nb= Node(15)
Nc= Node(25)
Nd= Node(35)

Na.next= Nb
Nb.next= Nc
Nc.next= Nd

head= Na
curr=head
print('original linked list')
while curr!=None:
    print(curr.data)
    curr= curr.next


curr= head
while curr.next.next!=None:
    curr=curr.next
curr.next= None
curr=head
print('After removing last node')
while curr!=None:
    print(curr.data)
    curr= curr.next

