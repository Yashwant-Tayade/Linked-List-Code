class Node:  
    def __init__(self):      
        self.data = 0
        self.next = None
        self.prev = None
def component(head_ref, refArr, n):
    if (head_ref == None):
        return 0;
  
    connectedComponents = 0;
  
    refSet = set()
    refSet.add(refArr[0]);
    connectedComponents += 1
    for i in range(1, n):
        refSet.add(refArr[i]);
  
        if (refArr[i].prev == None):
            if (refArr[i].next not in refSet):
                connectedComponents += 1
        elif (refArr[i].next == None):
            if (refArr[i].next not in refSet):
                connectedComponents += 1
        elif (refArr[i].prev in refSet
              and refArr[i].next in refSet):
            connectedComponents -= 1
        elif (refArr[i].prev not in refSet
              and refArr[i].next not in refSet):
            connectedComponents += 1
    return connectedComponents;
def push(head_ref, new_data):
    new_node = Node()
    current_node = new_node;
    new_node.data = new_data;
    new_node.prev = None;
    new_node.next = (head_ref);
    if ((head_ref) != None):
        (head_ref).prev = new_node;
    (head_ref) = new_node;
    return current_node, head_ref;
  
def printList(node):
    while (node != None):
        print(node.data, end = ' ');
        node = node.next;
         

if __name__=='__main__':
  
    head = None;

    ref_to_nodeN2, head = push(head, 2);
    ref_to_nodeN4, head = push(head, 4)
    ref_to_nodeN5, head = push(head, 5)
    ref_to_nodeN10, head = push(head, 10)
    ref_to_nodeN7, head = push(head, 7)
    ref_to_nodeN1, head = push(head, 1)  
    refArr = [ref_to_nodeN5, ref_to_nodeN2, ref_to_nodeN7, ref_to_nodeN1]
    connectedComponents = component(head, refArr, 4);
    print("Total number of connected components are ", connectedComponents)
 