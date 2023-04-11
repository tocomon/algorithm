import sys  
from itertools import permutations

n = int(input())
a=[]
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
mins=0
for _ in range(len(a)):
    mins+=sum(a[_])
#print(mins)

for perm in permutations(range(n)):
    s=0
    for i in range(n):
        if a[perm[i]][perm[(i+1)%n]]==0:
            s = mins
        elif a[perm[i]][perm[(i+1)%n]]!=0:
            s += a[perm[i]][perm[(i+1)%n]]
    mins=min(s,mins)

print(mins)
