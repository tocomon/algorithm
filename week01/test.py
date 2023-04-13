def cycle_length(n, num, cnt):
    a = num // 10        # 2
    b = num % 10         # 6
    c = (a + b) % 10     # 2 + 6 = 0"8"
    num = (b * 10) + c   # 60 + 8 = 68
    cnt = cnt + 1        # 사이클 수 + 1
    if(num == n):        # num에서 입력된 n과 똑같은 숫자(26)가 나오면 멈춤
        return cnt
    else:
        return cycle_length(n, num, cnt)

n = int(input())         
num = n
cnt = 0                  
print(cycle_length(n, num, cnt))
