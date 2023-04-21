from collections import deque

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# 방문 여부 체크
visited = [False] * (n + 1)

# dfs 개수
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)
