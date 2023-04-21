from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)



# from collections import deque

# def DFS(graph, root):
#     visited = []
#     stack = [root]

#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort(reverse=True)
#                 stack += temp
#     return " ".join(str(i) for i in visited)

# def BFS(graph, root):
#     visited = []
#     queue = deque([root])

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             if n in graph:
#                 temp = list(set(graph[n]) - set(visited))
#                 temp.sort()
#                 queue += temp
#     return " ".join(str(i) for i in visited)

# graph = {}
# n = input().split(' ')
# node, edge, start = [int(i) for i in n]
# for i in range(edge):
#     edge_info = input().split(' ')
#     n1, n2 = [int(j) for j in edge_info]
#     if n1 not in graph:
#         graph[n1] = [n2]
#     elif n2 not in graph[n1]:
#         graph[n1].append(n2)

#     if n2 not in graph:
#         graph[n2] = [n1]
#     elif n1 not in graph[n2]:
#         graph[n2].append(n1)
# #print(graph) # {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
# print(DFS(graph, start))
# print(BFS(graph, start))