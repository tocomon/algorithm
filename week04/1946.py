import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a=[]
    if n == 1:
        print(1)

    elif n == 2:
        p = input().strip()
        if p == "1 1" or p == "2 2":
            print(1)
        else:
            print(2)
    
    elif n > 2:

        for i in range(n):
            x, y = map(int, input().strip().split())
            a.append((x, y))
        
        a.sort(key=lambda x: x[0])

        if a[0] != (1,1):
            cnt=2
            maxx=a[0]
            a=a[1:]
            a.sort(key=lambda x: x[1])
            maxy=a[0]
            a=a[1:]
            for j in a:
                if j[0] > maxy[0] and j[1] > maxx[1]:
                    cnt+=1
            print(cnt)
        else:
            print(1)

    