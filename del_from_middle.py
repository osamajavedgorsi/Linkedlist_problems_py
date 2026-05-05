                              #Deleting node from kth position

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

Na= Node(2)
Nb= Node(4)
Nc= Node(6)
Nd= Node(8)
Ne= Node(10)

Na.next= Nb
Nb.next= Nc
Nc.next= Nd
Nd.next= Ne

head= Na
curr=head
print('original linked list')
while curr!=None:
    print(curr.data)
    curr= curr.next

#deleting with specific value
curr=head
while curr!=None:
    # print(curr.data)
    if curr.next.data==6:
        break
    curr= curr.next
curr.next= curr.next.next
curr=head
print('After deleting node containing value 6')
while curr!=None:
    print(curr.data)
    curr=curr.next
