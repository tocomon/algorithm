from collections import deque

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        print(stack)
        print(visited)
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
                # stack.extend(graph[n])
                #print(stack)
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                # temp = list(set(graph[n]) - set(visited))
                # temp.sort()
                # queue += temp
                queue.extend(graph[n])
    return " ".join(str(i) for i in visited)

  
graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
#print(graph) # {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
print(DFS(graph, start))
print(BFS(graph, start))