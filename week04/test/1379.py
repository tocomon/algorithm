import sys
import heapq
input = sys.stdin.readline

n = int(input())
room = [0] * (n+1)
lessonInfo = []
timeTable = []

for _ in range(n):
    no, start, end = map(int, input().split())
    lessonInfo.append([start, end, no])

lessonInfo.sort(key=lambda x: (x[0]))

answer = 0
for start, end, no in lessonInfo:
    if timeTable and timeTable[0][0] <= start:
        room[no] = room[timeTable[0][2]]
        heapq.heappop(timeTable)
    else:
        answer += 1
        room[no] = answer

    heapq.heappush(timeTable, [end, start, no])

print(answer)
for i in room[1:]:
    print(i)