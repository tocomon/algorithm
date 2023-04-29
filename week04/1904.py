# #시간초과
# import sys
# input=sys.stdin.readline
# n = int(input())

# def tile(x):
#     if x < 4:
#         return x
#     prev=2
#     curr=3
#     for i in range(4, x+1):
#         next = prev + curr
#         prev = curr
#         curr = next
        
#     return curr
# print(tile(n)%15746)


n = int(input())

# DP 테이블 초기화
dp = [0] * (n+1)
dp[1] = 1
if n >= 2:
    dp[2] = 2

# DP 진행
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

# 결과 출력
print(dp[n])
