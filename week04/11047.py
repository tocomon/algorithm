import sys
input = sys.stdin.readline

n, k = map(int, input().split())

stack=[]

for i in range(n):
    stack.append(int(input()))

cnt=0
for j in range(n):
    a=stack.pop()
    if a<=k:
        cnt+=k//a
        k=k%a

print(cnt)