import sys

num1 = int(sys.stdin.readline().strip())
num2 = int(sys.stdin.readline().strip())

num3 = num1 * (num2 % 10)  # 3번째 자리
num4 = num1 * ((num2 // 10) % 10)  # 4번째 자리
num5 = num1 * (num2 // 100)  # 5번째 자리
num6 = num1 * num2  # 6번째 자리

print(num3)
print(num4)
print(num5)
print(num6)