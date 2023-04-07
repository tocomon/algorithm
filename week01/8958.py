import sys
n = int(sys.stdin.readline())
a = [sys.stdin.readline()[:-1] for i in range(n)]  

b=[]
c=[]

for i in a:
    c=i.split("X")
    d=list(filter(lambda x: x.strip(), c))
    b.append(d)

f=[]
for j in b:
    e=[]
    for k in j:
        e.append(len(k))
    f.append(e)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


g=[]
for l in f:
    h=[]
    for m in l:
        z=0
        for i in range(m+1):
            z+=i
        h.append(z)

    g.append(sum(h))


for i in g:
    print(i)


    

