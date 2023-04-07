import sys
# n = sys.stdin.readline()
# N= int(n.split()[0])
# X= int(n.split()[1])
N, X = map(int,sys.stdin.readline().split())
A=[]
A=sys.stdin.readline().split()

result = ""
for a in A:
    if int(a) < X:
        result += str(a) + " "
result[:-1]



print(result)