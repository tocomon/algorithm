import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().rstrip().split())) for _ in range(n)]
cnt = [0,0] # 0,1의 개수

def dfs(x,y,n):
    # 시작 숫자
    num = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 시작 숫자와 다른 것이 나타나면
            if graph[i][j] != num:
                n //= 2
                # 4분할 탐색
                dfs(x,y,n)
                dfs(x+n,y,n)
                dfs(x,y+n,n)
                dfs(x+n,y+n,n)
                return
    cnt[num] += 1

dfs(0,0,n) # 0,0개부터 시작

print(cnt[0])
print(cnt[1])