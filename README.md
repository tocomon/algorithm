Python 알고리즘 문제 팁

sys.stdin.readline() > raw_input() > input()

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
a = list(map(int, input().split()))
a = [*map(int, input()), M]
a = [input() for i in range(n)] 
a = sorted([int(input()) for _ in range(n)])
a = [tuple(map(int, input().split())) for _ in range(n)]

while True:
    try:
        a.append(int(input()))
    except:
        break

print(*ans)
