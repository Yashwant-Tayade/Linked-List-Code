class point:
 
    def __init__(self, data):
        self.data = data  
        self.next = None  
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
 
def Circular(head):
    if head == None:
        return True
 
    node = head.next
    i = 0
 
    while((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
 
    return(node == head)
 
 
if __name__ == '__main__':
    obj = LinkedList()
    obj.head = point(1)
    second = point(2)
    third = point(3)
    fourth = point(4)
 
    obj.head.next = second
    second.next = third
    third.next = fourth
 
    if (Circular(obj.head)):
        print('Yes')
    else:
        print('No')
 
    fourth.next = obj.head
 
    if (Circular(obj.head)):
        print('Yes')
    else:
        print('No')
 