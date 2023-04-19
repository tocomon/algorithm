import heapq
import sys
n = int(sys.stdin.readline())
left_heap = []  # 중간값 이하의 값들을 저장하는 heap (max heap)
right_heap = []  # 중간값 이상의 값들을 저장하는 heap (min heap)

for i in range(n):
    x = int(sys.stdin.readline())

    # left_heap에 값을 추가하는 경우
    if not left_heap or x <= -left_heap[0]:
        heapq.heappush(left_heap, -x)
    # right_heap에 값을 추가하는 경우
    else:
        heapq.heappush(right_heap, x)

    # left_heap과 right_heap의 크기를 조절하여 중간값을 유지함
    if len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif len(right_heap) > len(left_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    # 중간값 출력
    print(-left_heap[0])
