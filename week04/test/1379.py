import sys,heapq
n = int(sys.stdin.readline())
load = []
queue = []
gang = [0]*n
room = 0
for _ in range(n):
    idx,s,e = map(int,sys.stdin.readline().split())
    load.append([s,e,idx-1])

load.sort()
for s,e,idx in load:
    if queue and queue[0][0] <= s:
        gang[idx] = gang[queue[0][2]]
        heapq.heappop(queue)
    else:
        room += 1
        gang[idx] = room
    heapq.heappush(queue,(e,s,idx))

print(room)
for i in gang:
    print(i)