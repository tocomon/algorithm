import sys

n = int(sys.stdin.readline())
for i in range(n):
    a=list(map(int, sys.stdin.readline().split()))
    mean = sum(a[1:])/a[0]
    n=0
    for i in a[1:]:
        if i>mean:
            n+=1
    result=n/a[0]*100
    print("{:.3f}%".format(result))

