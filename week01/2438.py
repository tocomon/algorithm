# 입력을 받을 때는 input() 함수를 사용합니다.
# 여러 줄 입력이 가능한 경우 for 루프를 사용합니다.

# 입력 받을 줄 수를 먼저 입력 받습니다.
import sys
n = int(sys.stdin.readline())

# n 줄에 걸쳐서 문자열을 입력 받습니다.

for i in range(n):
    stars = []
    star=""
    for j in range(n):
        star+="*"
        stars.append(star)

for i in range(n):
    print(stars[i])