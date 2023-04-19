import sys
import heapq

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

heap=[]

for i in a:
    heapq.heappush(heap,i)

sum = 0

if len(heap) ==1:
    print(0)
else:
    while len(heap)!=1:
        card = heapq.heappop(heap) + heapq.heappop(heap)
        sum += card
        heapq.heappush(heap,card)
    print(sum)