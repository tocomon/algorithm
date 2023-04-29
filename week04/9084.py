T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    N = int(input()) # 동전의 가지 수
    C = list(map(int, input().split())) # 동전의 가치
    M = int(input()) # 만들어야 할 금액
    D = [[0]*(M+1) for _ in range(N+1)] # D[i][j] : i번째까지의 동전으로 금액 j를 만드는 방법의 수
    for i in range(N+1):
        D[i][0] = 1 # 금액 0을 만드는 방법은 1가지 (아무 동전도 사용하지 않는 경우)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if j-C[i-1] >= 0:
                D[i][j] = D[i-1][j] + D[i][j-C[i-1]]
            else:
                D[i][j] = D[i-1][j]
            print(D)
    print(D[N][M])
