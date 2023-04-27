import sys
input = sys.stdin.readline


def skyline(buildings):
    
    if not buildings:
        return []
    
    #각 분할이 끝나면 해당 좌표로 변환 
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][1]], [buildings[0][2], 0]]
    
    #분할 과정    
    left = skyline(buildings[:len(buildings) // 2])
    right = skyline(buildings[len(buildings) // 2:])
    
    return merge(left, right)



#각각 나눠진 빌딩을 합치는 과정 
def merge(left, right):
    h1, h2 = 0, 0
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        
        if left[i][0] < right[j][0]:
            h1 = left[i][1]
            corner = left[i][0]
            i += 1
            
        elif right[j][0] < left[i][0]:
            h2 = right[j][1]
            corner = right[j][0]
            j += 1
            
        else:
            h1 = left[i][1]
            h2 = right[j][1]
            corner = right[j][0]
            i += 1
            j += 1
            
        if is_valid(result, max(h1,h2)):
            result.append([corner, max(h1, h2)])
    result.extend(right[j:])
    result.extend(left[i:])
    return result


def is_valid(result, new_height):
    return not result or result[-1][1] != new_height



n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

for i in skyline(arr):
    print(*i, end = ' ')



"""
import sys
from collections import defaultdict
from bisect import bisect_left #이진탐색

active = [0] # always sorted

def apply(iterable): #
    for a, i in iterable:
        idx = bisect_left(active, a) # active에서 a가 들어갈 index
        active[idx:idx+i] = [] if i else [a] # idx 부터 i 만틈 비우거나, [a] 값으로 대체

input = sys.stdin.readline
n = int(input())

start = defaultdict(list) # {1: [(11, 0)], 5: [(11, 1)]} 형태
for i in range(n):
    l, h, r = map(int, input().split())
    start[l].append((h, 0))
    start[r].append((h, 1))
# print("start: ", end='')
# print(start)

s = sorted(start.keys()) # s: [1, 2, 3, 5, 7, 9, 12, 14, 16, 19, 22, 23, 24, 25, 28, 29]
# print("s: ", end='')
# print(s)

m = 0 # 높이 저장
write = []

for i in s: 
    apply(start[i]) # 높이 체크
    # print("active " + str(i) + ": ", end='')
    # print(active)
    if m != active[-1]: # 높이 변화 체크
        m = active[-1]
        # print("active2: ", end='')
        # print(active)
        write.extend([i, m]) # 높이 변할 경우 출력
        # print("write: ", end='')
        # print(write)


print(*write)
"""