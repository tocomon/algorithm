N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for length in range(2, N+1):
    for i in range(N-length+1):
        j = i + length - 1
        dp[i][j] = float('inf') # 무한대
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + matrix[i][0] * matrix[k][1] * matrix[j][1] + dp[k+1][j]) # matrix[i] * matrix[k] * matrix[j]

print(dp[0][N-1])
