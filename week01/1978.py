import sys  
n = int(input())  
a = list(map(int, sys.stdin.readline().split()))

def is_prime(num):
    if num < 2:  # 1과 0은 소수가 아님
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime=0
for i in a:
    if is_prime(i):
        prime += 1

        

print(prime)