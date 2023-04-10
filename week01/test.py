import sys

N = int(sys.stdin.readline())
counts = [0] * 10001

# 각 숫자의 개수를 count
for i in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

# counts 배열을 처음부터 끝까지 순회하며 오름차순으로 출력
for i in range(10001):
    while counts[i] > 0:
        print(i)
        counts[i] -= 1
