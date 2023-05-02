import sys
input = sys.stdin.readline

a=input().strip().split('-')
num=0
for i in a[1:]:
    num += sum(map(int,i.split('+')))
result=sum(map(int,a[0].split('+')))-num

print(result)
