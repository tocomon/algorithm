# import sys
# input = sys.stdin.readline

# cnt = 0 

# n = int(input())

# a = []
# for _ in range(n):
#     a.append(list(map(int,input().strip().split())))

# dp = [[0] * (n+1) for _ in range(n+1)]

# cnt=0
# def find(x,y):
#     global cnt
#     if x==1 and y==1:
#         cnt+=1
#     else:
#         for i in range(x-1):
#             if i + 1 + a[y-1][i] == x:
#                 dp[i+1][y] = dp[x][y] +1
#                 find(i+1,y)
#         for j in range(y-1):
#             if j + 1 + a[j][x-1] == y:
#                 dp[j][x-1] = dp[x][y] +1
#                 find(x,j+1)

# find(n,n)
# print(dp)
# print(cnt)


import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 # 초기 값

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]
        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]