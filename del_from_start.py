                              #Deleting node from beginning

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

Na= Node(10)
Nb= Node(20)
Nc= Node(30)
Nd= Node(40)

Na.next= Nb
Nb.next= Nc
Nc.next= Nd

head= Na
curr=head
print('original linked list')
while curr!=None:
    print(curr.data)
    curr= curr.next
head= head.next
curr= head
print('After removing first node')
while curr!=None:
    print(curr.data)
    curr= curr.next

