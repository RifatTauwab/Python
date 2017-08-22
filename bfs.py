def bfs(start):
    queue = []
    visited =[False]*(V)
    
    queue.append(start)
    visited[start] = True
    
    while queue:
        n = queue.pop(0)
        print 'node',n
        for i in range(0,V):
            if (graph[n,i] == 1) and (visited[i]==False):
                queue.append(i)
                visited[i] = True


graph = {}
V = int(raw_input("enter vertex: "))
E = int(raw_input("enter edges: "))
for i in range(V):
    for j in range(E):
        graph[i,j] = 0
for i in range(0,E):
    node1 = int(raw_input("enter node1: "))
    node2 = int(raw_input("enter node2: "))
    graph[node1,node2] = 1
start = int(raw_input("enter start node: "))
bfs(start)
