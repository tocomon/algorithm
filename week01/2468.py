import sys  
n = int(input())
a=[]
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

sys.setrecursionlimit(10**8) # 10^8 까지 늘림. PyPy에 없음.

def para(a,k,l):
    if k==0 and l==0:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
    elif k==0 and l==n-1:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)
    elif k==n-1 and l==0:
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
    elif k==n-1 and l==n-1:
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)
    elif k==0:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)
    elif l==0:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)      
    elif k==n-1:
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)
    elif l==n-1:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)
    else:
        if a[k+1][l]!=0:
            a[k+1][l]=0
            para(a,k+1,l)
        if a[k][l+1]!=0:
            a[k][l+1]=0
            para(a,k,l+1)
        if a[k-1][l]!=0:
            a[k-1][l]=0
            para(a,k-1,l)
        if a[k][l-1]!=0:
            a[k][l-1]=0
            para(a,k,l-1)

maxa = max(map(max,a))


ns1=[]
for _ in range(maxa):
    ns2=[]
    for i in range(n):
        ns3=[]
        for j in range(n):
            if a[i][j]<=_:
                a[i][j]=0
            ns3.append(a[i][j])
        ns2.append(ns3)
    ns1.append(ns2)

#print(ns1)

max_count = 0
for _ in range(maxa):
    a=ns1[_]
    count=0
    for i in range(n):
        for j in range(n):
            if a[i][j]!=0:
                count+=1
                para(a,i,j)    
    max_count = max(max_count, count)

print(max_count)