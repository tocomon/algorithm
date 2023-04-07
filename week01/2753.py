import sys
a = int(sys.stdin.readline().strip())

if a%4==0 and a%100!=0:
    b=1
elif a%400==0:
    b=1
else:
    b=0

print(b)