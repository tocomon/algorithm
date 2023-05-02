import sys
input = sys.stdin.readline

n = int(input())

a=[]

for i in range(n):
    s, e = map(int,input().strip().split())
    a.append((s, e))

a.sort(key=lambda x: (x[1], x[0]))

end=0
count=0

for s, e in a:
    if s >= end:
        count += 1
        end=e
        
print(count)

