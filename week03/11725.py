import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node, parent, depth, graph, parent_list):
    parent_list[node] = parent
    for child in graph[node]:
        if child != parent:
            dfs(child, node, depth+1, graph, parent_list)

n = int(input())
graph = [[] for _ in range(n+1)]
parent_list = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0, 0, graph, parent_list)
print(graph)
print(parent_list)
for i in range(2, n+1):
    print(parent_list[i])



# # 틀렸습니다
# import sys
# from collections import deque
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline

# def dfs(start):
#     visited[start] = True      
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)

# def bfs(start):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)

# n = int(input())
# graph = [[] for _ in range(n+1)]

# for i in range(n-1):
#     try:
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     except:
#         break

# # 방문 여부 체크
# visited = [False] * (n + 1)

# dfs(1)

# for i in graph[2:]:
#     print(i[0])
