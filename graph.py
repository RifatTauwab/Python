graph = {}

for i in range(5):
    for j in range(5):
        graph[i,j] = 0
for i in range(0,5):
    node1 = int(raw_input("enter node1: "))
    node2 = int(raw_input("enter node2: "))
    graph[node1,node2] = 1

for i in range(5):
    for j in range(5):
        print graph[i,j],

    print '\n'


    
