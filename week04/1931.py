import sys
input = sys.stdin.readline

n = int(input())

a=[]

for i in range(n):
    s, e = map(int,input().strip().split())
    a.append((s, e))

a.sort(key=lambda x: (x[1], x[0]))

endtime=a[0][1]
count=1

for s, e in a[1:]:
    if s >= endtime:
        count += 1
        endtime=e
        
print(count)

