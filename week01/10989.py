import sys

n = int(sys.stdin.readline())

count = [0] * 10001  # 입력으로 주어지는 수는 10,000 이하의 자연수이다.

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
