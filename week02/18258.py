import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])




# 시간초과
# import sys
# queue=[]
# n=int(sys.stdin.readline())

# def func(k):
#     if k[0] == "pop":
#         if len(queue)>0:
#             poped=queue.pop(0)
#             print(poped)
#         else:
#             print(-1)
#     if k[0] == "size":
#         print(len(queue))
#     if k[0] == "empty":
#         if len(queue)==0:
#             print(1)
#         else:
#             print(0)
#     if k[0] == "front":
#         if len(queue)>0:
#             print(queue[0])
#         else:
#             print(-1)
#     if k[0] == "back":
#         if len(queue)>0:
#             print(queue[-1])
#         else:
#             print(-1)
#     if k[0] == "push":
#         queue.append(k[1]) 

# a = [sys.stdin.readline().strip().split() for i in range(n)] 


# for i in a:
#     func(i)