import sys
x, y = map(int,sys.stdin.readline().split())
n=int(sys.stdin.readline())
X=[0]
Y=[0]
X.append(x)
Y.append(y)  
for _ in range(n):
    d, s = map(int,sys.stdin.readline().split())
    if d == 0:
        Y.append(s)
    else:
        X.append(s)

X.sort()
Y.sort()
Num1=[]
Num2=[]
for i in range(0,len(X)-1):
    num1 = X[i+1]-X[i]
    Num1.append(num1)
for j in range(0,len(Y)-1):
    num2 = Y[j+1]-Y[j]
    Num2.append(num2)
result=max(Num1)*max(Num2)
print(result)