import sys  
n = int(input())  
a = [int(input()) for i in range(n)]
a.reverse()
see = a[0]

cnt=1
for i in range(1,len(a)):
    if a[i]>see:
        see=a[i]
        cnt+=1

print(cnt)