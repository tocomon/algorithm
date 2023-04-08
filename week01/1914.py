import sys
n = int(sys.stdin.readline())

a=[]
b=[]
c=[]

for i in range(n):
    a.append(i)

n=n-1

def hanoi(k):
    if k==0:
        return 1
    else:
        return 2**k + hanoi(k-1)

def move(n, start, end, temp):
    if n == 1:
        print(start, end)
    else:
        move(n-1, start, temp, end)
        print(start, end)
        move(n-1, temp, end, start)

if n >19:
    print(hanoi(n))
else:
    print(hanoi(n))
    move(n+1,1,3,2)


# 1 3 7 15 31
#  2 4 8 16

# 13

# 12
# 13
# 23

# 13
# 12
# 32
# 13
# 21
# 23
# 13

# 12
# 13
# 23
# 12
# 31
# 32
# 12
# 13
# 23
# 21
# 31
# 23
# 12
# 13
# 23





# n=1
# 1번
# 1 3

# n=2
# 3번
# 1 2
# 1 3
# 2 3

# n=3
# 7번
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

# n=4
# 15번
# 1 2
# 1 3
# 2 3
# 1 2
# 3 1
# 3 2
# 1 2
# 1 3
# 2 3
# 2 1
# 3 1
# 2 3
# 1 2
# 1 3
# 2 3




# 3 1 3 2

# 2 1 2 3   
# 1 3
# 2 2 3 1


# 1 1 3 2
# 1 2
# 1 3 2 1
# 1 3
# 1 2 1 3
# 2 3
# 1 1 3 2

# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3