import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def solution(n):
    lst = [sorted(list(map(int, input().split()))) for i in range(n)]
    lst.sort(key=lambda x: x[1])
    d = int(input())
    result = -1
    heap = []
    for s, e in lst:
        lim = e - d
        if s >= lim:
            heappush(heap, s)
        while heap and heap[0] < lim:
            heappop(heap)
        result = max(result, len(heap))
    print(result)

if __name__ == '__main__':
    solution(int(input()))

# 집과 사무실의 위치 모두 철로 선분에 포함되는 최대 사람 수

# 출력: 선분에 포함되는 최대 사람들의 수

# 체크할 조건
# 사람수 1 <= n <= 100000
# -1억 <= hi, oi <= 1억
# 철로 길이 1 <= d <= 2억

# 정렬해서 라인 스위핑.
# 끝 위치 기준으로 정렬.
# 선분 범위에 들어오면 heap에 넣는다.
# 선분 범위에 들어올 때까지 heappop
    # heap의 크기로 최대 사람 수를 갱신한다.




# import sys
# import heapq

# n = int(sys.stdin.readline())
# road_info = []
# for _ in range(n):
#     road = list(map(int, sys.stdin.readline().split()))
#     road_info.append(road)

# d = int(sys.stdin.readline())
# roads = []
# for road in road_info:
#     house, office = road
#     if abs(house - office) <= d:
#         road = sorted(road)
#         roads.append(road)
# roads.sort(key=lambda x:x[1])

# answer = 0
# heap = []
# for road in roads:
#     if not heap:
#         heapq.heappush(heap, road)
#     else:
#         while heap[0][0] < road[1] - d:
#             heapq.heappop(heap)
#             if not heap:
#                 break
#         heapq.heappush(heap, road)
#     answer = max(answer, len(heap))

# print(answer)