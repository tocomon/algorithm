import sys  
n = int(input())  
a = [int(sys.stdin.readline()) for i in range(n)]


def is_prime(num):
    if num < 2:  # 1과 0은 소수가 아님
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in a:
    for j in range(int(i/2)):
        num1=i/2+j
        num2=i/2-j
        if is_prime(num1) and is_prime(num2):
            print(str(int(num2)) + " " +str(int(num1)))
            break


