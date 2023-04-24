import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node, parent, graph, parent_list):
    parent_list[node] = parent      
    for child in graph[node]:
        if child != parent:
            dfs(child, node, graph, parent_list)

n = int(input())
graph = [[] for _ in range(n+1)]
parent_list = [0] * (n+1)

for i in range(n-1):
    try:
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

dfs(1, 0, graph, parent_list)

for i in parent_list[2:]:
    print(i)


# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline

# def dfs(node, parent, depth, graph, parent_list):
#     parent_list[node] = parent
#     for child in graph[node]:
#         if child != parent:
#             dfs(child, node, depth+1, graph, parent_list)

# n = int(input())
# graph = [[] for _ in range(n+1)]
# parent_list = [0] * (n+1)

# for i in range(n-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# dfs(1, 0, 0, graph, parent_list)
# print(graph)
# print(parent_list)
# for i in range(2, n+1):
#     print(parent_list[i])