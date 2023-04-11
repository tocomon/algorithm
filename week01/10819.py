import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

from itertools import permutations

max_sum = 0

for perm in permutations(a):
    s = 0
    #print(perm)
    for i in range(n - 1):
        s += abs(perm[i] - perm[i + 1])
    max_sum = max(max_sum, s)
    #print(max_sum)

print(max_sum)