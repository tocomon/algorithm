import sys  
n = int(input())  
a = [sys.stdin.readline().strip() for i in range(n)]  

# 스택 자료구조를 이용하여 괄호 문자열이 올바른 괄호 문자열인지 판단하는 함수
def is_valid_parenthesis(s):
    stack = []  # 스택

    for c in s:
        if c == '(':  # 열린 괄호인 경우
            stack.append(c)
        else:  # 닫힌 괄호인 경우
            if not stack:  # 스택이 비어있는 경우
                return False
            stack.pop()

    return not stack  # 스택이 비어있는 경우 True, 아닌 경우 False 반환

for _ in a:
    if is_valid_parenthesis(_):
        print('YES')
    else:
        print('NO')