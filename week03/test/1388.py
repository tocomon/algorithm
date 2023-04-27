n, m = map(int, input().split())

# 바닥 장식 입력받기
floor = []
for _ in range(n):
    floor.append(input())

# 각 행과 열에 대해 나무 판자 개수 세기
count = 0
for i in range(n):
    for j in range(m):
        # 이미 처리된 행 또는 열은 건너뛰기
        if floor[i][j] == '.':
            continue
        # '-'가 연속으로 나오는 경우
        if floor[i][j] == '-':
            k = j
            while k < m and floor[i][k] == '-':
                floor[i] = floor[i][:k] + '.' + floor[i][k+1:]
                k += 1
            count += 1
        # '|'가 연속으로 나오는 경우
        elif floor[i][j] == '|':
            k = i
            while k < n and floor[k][j] == '|':
                floor[k] = floor[k][:j] + '.' + floor[k][j+1:]
                k += 1
            count += 1

print(count)
