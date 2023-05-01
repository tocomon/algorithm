import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# DP로 푸는 법
dp = [1] * n  # DP 테이블 초기화

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:  # 현재 값보다 작은 값이 있다면
            dp[i] = max(dp[i], dp[j] + 1)  # 해당 위치까지의 최장 부분 수열 길이 갱신

print(max(dp))  # 최장 부분 수열 길이 출력
