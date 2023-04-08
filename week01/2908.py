import sys  
a = list(sys.stdin.readline().split())
num1 = a[0][2]+a[0][1]+a[0][0]
num2 = a[1][2]+a[1][1]+a[1][0]
num1 = int(num1)
num2 = int(num2)
if num1> num2:
    print(num1)
else:
    print(num2)
