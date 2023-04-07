import sys  

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

n =a*b*c

for i in range(10):
    count=0
    for j in str(n):
        if i == int(j):
            count+=1

    print(count)


