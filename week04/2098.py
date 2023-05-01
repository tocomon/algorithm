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

# print()


# #######################################################
# import sys
# input = sys.stdin.readline

# n = int(input())
# matrix = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     matrix.append(a)

# # Floyd-Warshall 알고리즘을 이용하여 모든 쌍 최단 경로를 구함
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][k] != 0 and matrix[k][j] != 0:
#                 if matrix[i][j] == 0 or matrix[i][j] > matrix[i][k] + matrix[k][j]:
#                     matrix[i][j] = matrix[i][k] + matrix[k][j]

# # 최소 비용 경로 출력
# print(matrix[0][n-1])
# #########################################################






import sys

INF = sys.maxsize

# 비트 마스킹을 사용하여 현재까지 방문한 도시를 표시
def tsp_dp(n, w):
    # dp 배열 초기화
    dp = [[-1] * (1 << n) for _ in range(n)]

    # 출발 도시에서 출발 도시로 돌아오는 경우
    # 모든 도시를 방문한 경우 최소 비용은 0
    for i in range(n):
        dp[i][1 << i] = 0

    for s in range(1, (1 << n)):
        for i in range(n):
            # i번 도시가 비트 마스킹에 포함되어 있지 않으면 건너뛰기
            if not (s & (1 << i)):
                continue
            for j in range(n):
                # j번 도시가 비트 마스킹에 포함되어 있거나,
                # i와 j번 도시가 같은 경우 건너뛰기
                if s & (1 << j) or i == j:
                    continue
                if dp[i][s] == -1:
                    continue
                # i에서 j로 이동하는 경우의 비용 계산
                cost = dp[i][s] + w[i][j]
                if dp[j][s | (1 << j)] == -1 or dp[j][s | (1 << j)] > cost:
                    # 이전에 계산한 최소 비용보다 현재 계산한 비용이 더 작은 경우 갱신
                    dp[j][s | (1 << j)] = cost

    # 모든 도시를 방문하고 다시 출발 도시로 돌아오는 경우의 최소 비용 반환
    return min(dp[i][(1 << n) - 1] + w[i][0] for i in range(n) if dp[i][(1 << n) - 1] != -1)

# 입력 예시
n = 4
w = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]

# 결과 출력
print(tsp_dp(n,w))
