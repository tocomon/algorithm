import sys  
n = int(input())  
a = [int(sys.stdin.readline()) for i in range(n)]  

stack=[]
for i in a:
    if i !=0:
        stack.append(i)
    else:
        stack.pop(-1)

print(sum(stack))