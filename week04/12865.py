import sys  
input = sys.stdin.readline

n, k = map(int,input().split())

w = [0] * (n+1) # weight
v = [0] * (n+1) # value
for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

# dp[i][j] : i번째 물건을 고려하고, 배낭의 무게 한계가 j일 때, 넣을 수 있는 물건들의 최대 가치합
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < w[i]:  # i번째 물건을 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]
        else:  # i번째 물건을 넣을 수 있는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(dp[n][k])
