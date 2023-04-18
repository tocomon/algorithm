n = int(input())
heights = list(map(int, input().split()))

stack = []
ans = []

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            ans.append(stack[-1][0] + 1)
            break
        stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, heights[i]])

print(*ans)





# 시간초과
# import sys  
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))

# receive=[0]

# def check(k):
#     for i in range(len(a)):
#         b = a[i]
#         for j in range(0,i):
#             if b < a[-len(a)+i-j-1]:
#                 receive.append(i-j)
#                 break
#         if len(receive) != i+1:
#             receive.append(0)
    
# check(a)

# print(' '.join(str(x) for x in receive))



