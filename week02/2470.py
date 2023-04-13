from itertools import combinations
import sys

n = int(sys.stdin.readline())
a = list(map(int, input().split()))

result=0
for com in combinations(a,2):
    sum(com)
