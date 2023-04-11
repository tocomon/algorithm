def n_queen(n):
    count = 0
    # 각 열에 퀸을 놓는 방법을 저장하는 리스트
    # 초기값은 모두 0으로 설정
    column = [0] * n
    # 대각선 방향에 퀸이 있는지 여부를 저장하는 리스트
    # 초기값은 모두 False로 설정
    diagonal1 = [False] * (2 * n - 1)  # 왼쪽에서 오른쪽 아래로 향하는 대각선
    diagonal2 = [False] * (2 * n - 1)  # 오른쪽에서 왼쪽 아래로 향하는 대각선
    
    # 백트래킹 함수
    def backtrack(row):
        nonlocal count
        # 모든 행에 퀸을 놓았으면 경우의 수 1 추가
        if row == n:
            count += 1
            return
        # 현재 행에서 가능한 열에 퀸을 놓아보기
        for col in range(n):
            if not column[col] and not diagonal1[row + col] and not diagonal2[row - col + n - 1]:
                column[col] = True
                diagonal1[row + col] = True
                diagonal2[row - col + n - 1] = True
                backtrack(row + 1)
                column[col] = False
                diagonal1[row + col] = False
                diagonal2[row - col + n - 1] = False
    
    # 첫 번째 행부터 백트래킹 시작
    backtrack(0)
    return count

import sys
n = int(sys.stdin.readline())
print(n_queen(n))




n = int(input())
lst = [0]*n
ans = 0
def queen(a):
    global ans
    if a == n:
        ans += 1
        return
    else:
        for i in range(n):
            lst[a] = i
            if check(a):
                queen(a+1)
def check(a):
    for i in range(a):
        if lst[a] == lst[i] or abs(lst[a]-lst[i]) == abs(a-i):
            return False
    return True
queen(0)
print(ans)