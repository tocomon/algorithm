# 입력 받기
n, m = map(int, input().split())
h_lines = [0] * (n + 1) # 가로 점선 위치를 저장하는 리스트
v_lines = [0] * (m + 1) # 세로 점선 위치를 저장하는 리스트
k = int(input())
for i in range(k):
    direction, pos = map(int, input().split())
    if direction == 0: # 가로 점선일 때
        h_lines[pos] = 1
    else: # 세로 점선일 때
        v_lines[pos] = 1

# 가장 긴 가로 조각과 세로 조각 구하기
h_lengths = []
prev_h = 0
for i in range(1, n + 1):
    if h_lines[i] == 1:
        h_lengths.append(i - prev_h)
        prev_h = i
h_lengths.append(n + 1 - prev_h)

v_lengths = []
prev_v = 0
for i in range(1, m + 1):
    if v_lines[i] == 1:
        v_lengths.append(i - prev_v)
        prev_v = i
v_lengths.append(m + 1 - prev_v)

# 가장 큰 종이 조각의 넓이 구하기
max_area = 0
for h_length in h_lengths:
    for v_length in v_lengths:
        area = h_length * v_length
        if area > max_area:
            max_area = area

print(max_area)
