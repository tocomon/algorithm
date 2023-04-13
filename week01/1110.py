n = int(input())
cnt = 0
num = n

while True:
    cnt += 1
    a = num // 10 # 첫 번째 자리 수
    b = num % 10 # 두 번째 자리 수
    c = (a + b) % 10 # 두 수의 합의 마지막 자리 수
    num = b * 10 + c # 새로운 수 생성
    if num == n: # 처음 수와 같아지면 종료
        break
        
print(cnt)
