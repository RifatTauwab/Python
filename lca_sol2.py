class Node:
    def __init__(self, value, parent): 
        self.value = value 
        self.parent = parent

def get_lca(node1, node2): 
    path_node1 = []
    common = None
    
    if node1 == None and node2==None:
        return None
    elif node1==None:
        return node2
    elif node2==None:
        return node1
    
    while node1:
        path_node1.append(node1.value)
        node1 = node1.parent
    while node2:
        if node2.value in path_node1:
            common = node2.value
            break
        node2 = node2.parent
    return common
     


    
    

root = Node(1, None) 
left_2 = Node(2, root) 
right_3 = Node(3, root) 
left_4 = Node(4, left_2)
right_5 = Node(5, left_2) 
left_6 = Node(6, right_3) 
right_7 = Node(7, right_3)
left_8 = Node(8, left_4)
right_9 = Node(9, left_4)

print(get_lca(right_5,left_8))
print(get_lca(left_8,right_7))
print(get_lca(left_4,right_5))
