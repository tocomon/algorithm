# input
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5


import sys

N = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().split()))

a.sort()  # 이분 탐색을 위해 배열 a를 정렬합니다.

for i in range(M):
    left = 0
    right = N - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b[i]:
            found = True
            
            break
        elif a[mid] < b[i]:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        print(1)
    else:
        print(0)


# output
# 1
# 1
# 0
# 0
# 1


# 시간 초과
# import sys 
# N = int(sys.stdin.readline().strip())
# a = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline().strip())
# b = list(map(int, sys.stdin.readline().split()))

# result=[]
# for i in range(M):
#     result.append(0)
#     for j in range(N):
#         if b[i]==a[j]:
#             result.pop(-1)
#             result.append(1)
#             break

# print(result)
    