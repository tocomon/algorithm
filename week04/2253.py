import sys
from collections import deque

# 입력 받기
n, m = map(int, input().split())
small_stones = set()
for _ in range(m):
    stone = int(input())
    small_stones.add(stone)

# bfs로 최소 점프 횟수 구하기
def bfs():
    q = deque([(1, 1)])  # (현재 위치, 현재 속도)
    visited = {(1, 1)}
    while q:
        pos, speed = q.popleft()
        # N번 돌에 도착한 경우
        if pos == n:
            return speed - 1
        # 가능한 점프 거리를 계산하여 다음 위치와 속도를 구함
        for dist in range(-1, 2):
            next_pos = pos + speed + dist
            next_speed = speed + dist
            # 다음 위치가 유효하고 큰 돌이 있는 경우
            if 1 <= next_pos <= n and next_pos not in small_stones and (next_pos, next_speed) not in visited:
                visited.add((next_pos, next_speed))
                q.append((next_pos, next_speed))
    return -1

# 결과 출력
result = bfs()
print(result)
