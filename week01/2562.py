import sys  
#N, X = map(int,sys.stdin.readline().split())


n = 9
a = [int(sys.stdin.readline()) for i in range(n)]  
# a = ["1 2 3", "4 5 6"]
# print(a)
m=max(a)
print(m)
print(a.index(m)+1)