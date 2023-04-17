import sys

# 행렬의 크기 N과 B
n, b = map(int, input().split())

# 행렬 A를 입력받음
a = [list(map(int, input().split())) for _ in range(n)]

# 단위 행렬을 만드는 함수
def identity_matrix(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

# 행렬의 곱셈을 계산하는 함수
def multiply_matrix(a, b):
    n = len(a)
    m = len(b[0])
    ret = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(b)):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= 1000
    return ret

# A^B를 계산하는 함수
def pow_matrix(a, b):
    # 단위 행렬을 만듦
    ret = identity_matrix(n)
    # 지수를 이진수로 변환하여 거듭제곱을 계산
    while b > 0:
        if b % 2 == 1:
            ret = multiply_matrix(ret, a)
        a = multiply_matrix(a, a)
        b //= 2
    return ret

# A^B를 계산하여 출력
result = pow_matrix(a, b)
for row in result:
    print(" ".join(map(str, row)))
