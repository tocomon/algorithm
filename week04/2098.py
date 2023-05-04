import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # i to j value

dp = [[0] * (2 ** (N - 1)) for _ in range(N)]

def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (2 ** (N - 1)) - 1:
        if W[i][0]:
            return W[i][0]
        else:
            return float('inf')
            
    min_dist = float('inf')

    for j in range(1, N):
        if not W[i][j]:
            continue
        if route & (2 ** (j - 1)):
            continue
        dist = W[i][j] + solution(j, route | (2 ** (j - 1))) # 재귀
        if min_dist > dist:
            min_dist = dist

    dp[i][route] = min_dist
    
    return min_dist

print(solution(0, 0))


# import sys
# input = sys.stdin.readline

# n=int(input())
# matrix=[]
# for i in range(n):
#     a = list(map(int, input().split()))
#     matrix.append(a)

# w=[[float('inf')]*n for _ in range(n)]

# for i in range(n):
#     for j in range(i):
#         k=i-j+1
#         if w[i][j] != 0 and w[i][k] != 0 and w[k+1][j] !=0 and matrix[k][k+1] != 0:
#             w[i][j] = min(w[i][j], w[i][k] + matrix[k][k+1] + w[k+1][j])