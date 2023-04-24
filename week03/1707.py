import sys
from collections import deque

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(start):
    global isValid
    visited[start] = True 
    for i in graph[start]:
        if not visited[i]:
            check[i] = (check[start]+1)%2 # ?
            print(check)
            dfs(i)
        elif check[start] == check[i]:
            isValid =False

n = int(input())

for i in range(n):
    isValid = True # 이분 그래프 판단
    v, e= map(int, input().split())
    visited = [False] * (v + 1)
    graph = [[] for _ in range(v+1)]
    check = [0] * (v+1) # 노드색 1 0 
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v+1):
        if isValid:
            dfs(i)
        else:
            break
    if isValid:
        print("YES")
    else:
        print("NO")

