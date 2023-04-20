import sys
from collections import defaultdict as dd
from bisect import bisect_left as bl

active = [0] # always sorted


def apply(iterable):
    for a, i in iterable:
        idx = bl(active, a)
        active[idx:idx+i] = [] if i else [a]


input = sys.stdin.readline
n = int(input())

start = dd(list)
for i in range(n):
    l, h, r = map(int, input().split())
    start[l].append((h, 0))
    start[r].append((h, 1))

s = sorted(start.keys())
m = 0
write = []

for i in s:
    apply(start[i])
    if m != active[-1]:
        m = active[-1]
        write.extend([i, m])

print(*write)