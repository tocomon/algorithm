import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt += 1
    # 상하좌우 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt_list = []

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
for c in cnt_list:
    print(c)
