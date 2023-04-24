import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 체크
visited = [False] * (n + 1)

# dfs
dfs(1)
print(sum(visited)-1)
