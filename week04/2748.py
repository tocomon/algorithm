import sys
input = sys.stdin.readline

# def fibo(x):
#     if x==0:
#         return 0
#     elif x==1:
#         return 1
#     return fibo(x-1)+fibo(x-2)

def fibo(x):
    if x < 2:
        return x
    
    prev = 0
    curr = 1
    
    for i in range(2, x+1):
        next = prev + curr
        prev = curr
        curr = next
        
    return curr


print(fibo(int(input())))