from sys import stdin

n, k = map(int, stdin.readline().split())

li =[]

for i in range(n):
   li.append(int(stdin.readline().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])


# # BFS
# from collections import deque
# import sys
# input=sys.stdin.readline

# n, value = map(int, input().split())
# coins=list(set(int(input()) for _ in range(n)))
# check=[0 for _ in range(value+1)] ### 중복된 조합 filter해서 빼주는 효과가 있음// 없으면 메모리 초과난다 ..!

# def bfs(coins, value):
#     queue=deque()
#     for coin in coins:
#         if coin<value:
#             queue.append([coin,1])
#             check[coin]=1

#     while queue:
#         cum, cnt=queue.popleft()
#         if value==cum:
#             print(cnt)
#             break
#         for coin in coins:
#             cum1=cum+coin
#             cnt1=cnt+1
#             if cum1>value:
#                 continue
#             elif cum1<=value and check[cum1]==0:
#                 check[cum1]=1
#                 queue.append([cum1,cnt1])
            
#     if cum!=value:
#         print('-1')

# bfs(coins,value)
