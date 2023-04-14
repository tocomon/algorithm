n = int(input())
a = list(map(int, input().split()))


# # DP로 푸는 법
# dp = [1] * n  # DP 테이블 초기화

# for i in range(1, n):
#     for j in range(i):
#         if a[j] < a[i]:  # 현재 값보다 작은 값이 있다면
#             dp[i] = max(dp[i], dp[j] + 1)  # 해당 위치까지의 최장 부분 수열 길이 갱신

# print(max(dp))  # 최장 부분 수열 길이 출력


# binary search
def binary_search(arr, target):
    """
    arr: 이분 탐색을 수행할 리스트
    target: 탐색할 대상 값
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


def lis(arr):
    """
    arr: LIS를 구할 리스트
    """
    lis_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > lis_arr[-1]:
            lis_arr.append(arr[i])
        else:
            idx = binary_search(lis_arr, arr[i])
            lis_arr[idx] = arr[i]

    return len(lis_arr)

print(lis(a))