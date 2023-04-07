import sys  
a = list(map(int, sys.stdin.readline().split()))
# a = [1, 2, 3, 4, 5]
x=a[0]
y=a[1]
w=a[2]
h=a[3]

print(min(x,y,w-x,h-y))