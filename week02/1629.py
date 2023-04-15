# import sys  
# a,b,c = list(map(int, sys.stdin.readline().split()))

# result = pow(a,b,c)
# print(result)


def power(base, exponent, modulus):
    if exponent == 0:
        return 1 % modulus
    elif exponent % 2 == 0:
        return power(base**2 % modulus, exponent//2, modulus)
    else:
        return base * power(base, exponent-1, modulus) % modulus

a, b, c = map(int, input().split())
result = power(a, b, c)
print(result)
