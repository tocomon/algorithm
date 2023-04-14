import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()  # 용액을 특성값의 오름차순으로 정렬

left, right = 0, n-1  # 왼쪽 포인터와 오른쪽 포인터 초기화
result = (arr[left], arr[right])  # 현재 가장 0에 가까운 용액 조합

while left < right:
    mix = arr[left] + arr[right]  # 현재 조합의 특성값
    if abs(mix) < abs(sum(result)):  # 현재 조합이 더 0에 가까운 경우
        result = (arr[left], arr[right])  # 결과 갱신
        if mix == 0:  # 0에 정확히 맞는 용액이면 바로 종료
            break
    if mix > 0:  # 합이 양수이면 오른쪽 포인터를 왼쪽으로 한 칸 옮김
        right -= 1
    else:  # 합이 음수이면 왼쪽 포인터를 오른쪽으로 한 칸 옮김
        left += 1

print(*result)
