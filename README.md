Python 알고리즘 문제 팁

sys.stdin.readline() > raw_input() > input()

import sys <br>
input = sys.stdin.readline <br>
sys.setrecursionlimit(10**8) <br>

a = list(map(int, input().split())) <br>
a = [*map(int, input()), M] <br>
a = [input() for i in range(n)] <br>
a = sorted([int(input()) for _ in range(n)]) <br>
a = [tuple(map(int, input().split())) for _ in range(n)] <br>

while True:
    try:
        a.append(int(input()))
    except:
        break

print(*ans)
