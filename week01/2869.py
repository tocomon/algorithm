import sys  
import math
a = list(map(int, sys.stdin.readline().split()))
# a = [1, 2, 3, 4, 5]
i=0

goal = a[2]-a[1]
move = a[0]-a[1]

n=math.ceil(goal/move)
n=int(n)
print(n)